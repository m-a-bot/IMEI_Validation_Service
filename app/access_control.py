from http.client import HTTPException

from app.common.logging import log_decorator
from app.config import settings
from app.integrations.factories import AccessControlServiceBuilder


@log_decorator
async def user_wrapper(token: str):
    try:
        access_control_service = AccessControlServiceBuilder.build_service(
            settings
        )

        await access_control_service.verify_token(token)

    except Exception as ex:
        raise HTTPException(400, "Bad request")
