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

    async def verify_token(self, user_id: int, token: str):
        await send_request(
            endpoint=self.url,
            method="post",
            query_params={"user_id": user_id, "token": token},
            headers={},
        )
