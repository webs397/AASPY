from aiohttp import web
import logging
import json

logging.basicConfig(level=logging.DEBUG)



async def pass_json(request):
        data = {"aaslist": ["0 : ExampleMotor : [IRI] http://customer.com/aas/9175_7013_7091_9168 : ./aasxs/Example_AAS_ServoDCMotor_21.aasx"]}
        return web.json_response(data)




class MultipleAASView(web.View): #See https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_repository_http_rest_api/v1#/

    async def get_shells(self):
        return await pass_json(self)
        #raise NotImplementedError

    async def request_shell(self, request):
        raise NotImplementedError

    async def get_shell(self): #Duplicate of GET request_shell
        raise NotImplementedError

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

class SingleAASView(web.View): #See https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_http_rest_api/v1#/
    pass



        

app = web.Application()

# Routes from https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_repository_http_rest_api/v1#/
app.add_routes([web.view('/shells', MultipleAASView.get_shells),
                web.view('/shells/{aasId}', MultipleAASView.request_shell),
                web.view('/shells/{aasId}/aas', MultipleAASView.get_shell),
                web.view('/shells/{aasId}/aas/submodels', MultipleAASView.get_shell),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}', MultipleAASView.request_shell),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel', MultipleAASView.get_subModel),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/values', MultipleAASView.get_subModelValues),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements', MultipleAASView.get_subModelElements),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{seIdShortPath}', MultipleAASView.request_subModelElement),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{seIdShortPath}/value', MultipleAASView.request_subModelElementValue),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{idShortPathToOperation}/invoke', MultipleAASView.post_subModelOperation),
                web.view('/shells/{aasId}/aas/submodels/{submodelIdShort}/submodel/submodelElements/{idShortPathToOperation}/invocationList/{requestId}', MultipleAASView.get_subModelOperationResult)])

# Routes from https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_http_rest_api/v1#/
# app.add_routes([])

#Custom Routes to work with AASPE
app.add_routes([web.view('/server/listaas', MultipleAASView.get_shells),
                web.view('/aas/0/core', MultipleAASView.get_shell)]) # AASPE tries to access this; It's a GET request for the Shell with index 0


web.run_app(app)