from app.common.logging import log_decorator
from app.integrations.send_request import send_request
from app.interfaces.access_control_service_interface import (
    IAccessControlService,
)


class AccessControlService(IAccessControlService):
    def __init__(self, service_url: str):
        self.__url = service_url

    def __str__(self):
        return "Auth Service"

    @property
    def url(self):
        return self.__url

    @log_decorator
    async def verify_token(self, token: str):
        await send_request(
            endpoint=self.url,
            method="post",
            query_params={"token": token},
            headers={},
        )
