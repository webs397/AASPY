from aiohttp import web
import logging

logging.basicConfig(level=logging.DEBUG)

class MultipleAASView(web.View): #See https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_repository_http_rest_api/v1#/

    async def get_shells(self):
        raise NotImplementedError
        pass

    async def request_shell(self, request):
        raise NotImplementedError

    async def get_shell(self): #Duplicate of GET request_shell
        raise NotImplementedError

    async def get_subModels(self):
        raise NotImplementedError


class SingleAASView(web.view): #See https://app.swaggerhub.com/apis/BaSyx/basyx_asset_administration_shell_http_rest_api/v1#/
    pass



        

app = web.Application()


app.add_routes([web.view('/shells', MultipleAASView.get_shells),
                web.view('/shells/{aasId}', MultipleAASView.request_shell),
                web.view('/shells/{aasId}/aas', MultipleAASView.get_shell),
                web.view('/shells/{aasId}/aas/submodels', MultipleAASView.get_shell)])



















web.run_app(app)