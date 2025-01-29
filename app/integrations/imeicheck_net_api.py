from typing import Any
from urllib.parse import urljoin

from app.config import settings
from app.integrations.send_request import send_request
from app.interfaces.imei_check_api_interface import IBaseIMEICheckAPI
from app.schemes.pyd import IMEICheck


class IMEICheckNetAPI(IBaseIMEICheckAPI):

    def __init__(self, service_url: str, service_token: str):
        self.__url = service_url
        self.__token = service_token

    def __str__(self):
        return "imeicheck.net"

    @property
    def url(self) -> str:
        return self.__url

    @property
    def token(self) -> str:
        return self.__token

    async def check(self, imei_check: IMEICheck) -> dict[Any, Any]:
        url = urljoin(self.url, settings.IMEI_CHECKS_URL)

        body = imei_check.model_dump_json()

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept-Language": "en",
            "Content-Type": "application/json",
        }
        imei_verification_info = await send_request(
            endpoint=url, method="POST", data=body, headers=headers
        )
        return dict(imei_verification_info)
