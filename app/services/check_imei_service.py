from typing import Any

from fastapi import HTTPException
from typing_extensions import Unpack

from app.config import settings
from app.integrations.factories import IMEICheckAPIBuilder
from app.schemes.pyd import IMEICheck


class CheckIMEIService:
    def __init__(self, imei_api_name: str):
        self.imei_api = IMEICheckAPIBuilder.build_service(
            imei_api_name=imei_api_name, settings=settings
        )

    def __str__(self) -> str:
        return "Check IMEI Service"

    async def check(self, *args: Unpack[Any], **kwargs: Any):
        try:
            data = await self.imei_api.check(*args, **kwargs)
            return data
        except Exception as exc:
            raise HTTPException(404, exc)
