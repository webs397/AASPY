import zipfile
from aiohttp import web
import logging
import json
import testAASData
import pyecma376_2
from submodelelement import submodelelement
from submodelevent import submodelevent
from packaging import Event
from edgeNode import EdgeNode
import asyncio
from contextlib import suppress


logging.basicConfig(level=logging.DEBUG)

edgeNode = EdgeNode("Dummy", 1)


async def pass_json(request):
        data = {"aaslist": ["0 : ExampleMotor : [IRI] http://customer.com/aas/9175_7013_7091_9168 : ./aasxs/Example_AAS_ServoDCMotor_21.aasx"]}
        return web.json_response(data)



class Handler:

    def __init__(self):
        pass
        #self.models = models

    async def get_shells(self, request):
        return await pass_json(self)
        #raise NotImplementedError

    async def request_shell(self, request):
        raise NotImplementedError

    async def get_shell(self, request): #Duplicate of GET request_shell
        data = testAASData.coreAAS
        return web.json_response(data)
        #raise NotImplementedError

    async def get_subModels(self):
        raise NotImplementedError

    async def request_shell(self, request):
        raise NotImplementedError

    async def get_subModel(self):
        raise NotImplementedError

    async def get_subModelValues(self):
        raise NotImplementedError

    async def  get_subModelElements(self):
        raise NotImplementedError

    async def request_subModelElement(self):
        raise NotImplementedError

    async def request_subModelElementValue(self):
        raise NotImplementedError
    
    async def post_subModelOperation(self):
        raise NotImplementedError
    
    async def get_subModelOperationResult(self):
        raise NotImplementedError

    async def get_downloadShell(self, request):
        #data = open("C:\\Users\\benev\\OneDrive\\Documents\\BA_WS\\Code\\AASPY\\Example_AAS_ServoDCMotor_21.aasx", encoding="utf-8")
        #data = zipfile.ZipFile("C:\\Users\\benev\\OneDrive\\Documents\\BA_WS\\Code\\AASPY\\Example_AAS_ServoDCMotor_21.aasx",mode="r")
        return web.FileResponse('C:\\Users\\benev\\OneDrive\\Documents\\BA_WS\\Code\\AASPY\\Example_AAS_ServoDCMotor_21.aasx', headers={
            'Content-Disposition': 'Attachment;Example_AAS_ServoDCMotor_21.aasx'})
    
    async def get_eventMessages(self, request):
        SME1 = submodelelement()
        SME1.generate_dummy("RotationSpeed", 0, edgeNode.value)
        SME2 = submodelelement()
        SME2.generate_dummy("Torque", 1, edgeNode.value)
        SMEE = submodelevent()
        SMEE.generate_dummy()
        event = Event()
        event.generate_event(SME1, SMEE)
        #event.generate_event(SME2, SMEE)
        event.events = json.dumps(event.events)
        return web.json_response(json.loads(event.events), status=200)
        raise NotImplementedError



app = web.Application()
handler = Handler()
# Routes from https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_repository_http_rest_api/v1#/
app.add_routes([web.view('/shells', handler.get_shells),
                web.view('/shells/{aasId}', handler.request_shell),
                web.view('/shells/{aasId}/aas', handler.get_shell),
                web.view('/shells/{aasId}/aas/submodels', handler.get_shell),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}', handler.request_shell),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel', handler.get_subModel),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/values', handler.get_subModelValues),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements', handler.get_subModelElements),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{seIdShortPath}', handler.request_subModelElement),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{seIdShortPath}/value', handler.request_subModelElementValue),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{idShortPathToOperation}/invoke', handler.post_subModelOperation),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{idShortPathToOperation}/invocationList/{requestId}', handler.get_subModelOperationResult)])



# Routes from https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_http_rest_api/v1#/
# app.add_routes([])

#Custom Routes to work with AASPE
app.add_routes([web.view('/server/listaas', handler.get_shells),
                web.view('/aas/0/core', handler.get_shell), # AASPE tries to access this; It's a GET request for the Shell with index 0
                web.view('/server/getaasx/0', handler.get_downloadShell), #Downloads the shell with index 0
                web.view('/aas/0/geteventmessages', handler.get_eventMessages),
                web.view('/aas/0/geteventmessages/time/{tail:.*}', handler.get_eventMessages)]) 



async def listen_to_redis(app):
    try:
        await edgeNode.run()
    except asyncio.CancelledError:
        pass


async def background_tasks(app):
    app['redis_listener'] = asyncio.create_task(listen_to_redis(app))

    yield

    app['redis_listener'].cancel()
    await app['redis_listener']


async def run_other_task(_app):
    task = asyncio.create_task(edgeNode.run())

    yield

    task.cancel()
    with suppress(asyncio.CancelledError):
        await task  # Ensure any exceptions etc. are raised.

app.cleanup_ctx.append(run_other_task)


web.run_app(app)













# if __name__ == "__main__":
#     app = web.Application()
#     handler = Handler({'default': None})

#     app.router.add_get("/aas", handler.get_aas_detail)
#     app.router.add_get("/aas/submodels", handler.get_submodel_list)
#     app.router.add_get("/aas/submodels/{submodelIdShort}", handler.get_submodel_detail)
#     app.router.add_post("/aas/submodels/{submodelIdShort}", handler.put_submodel_detail)
#     app.router.add_delete("/aas/submodels/{submodelIdShort}", handler.delete_submodel_detail)
#     # usw.

#     web.run_app(app)