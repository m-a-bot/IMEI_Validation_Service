from app.interfaces.access_control_service_interface import (
    IAccessControlService,
)


class AccessControlServiceStub(IAccessControlService):
    def __init__(self, service_url: str):
        self.__url = service_url

    def __str__(self):
        return "Auth Service Stub"

    @property
    def url(self):
        return self.__url

    async def verify_token(self, token: str):
        return True
