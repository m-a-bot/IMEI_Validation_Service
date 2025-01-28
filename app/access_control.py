from http.client import HTTPException

from app.config import settings
from app.integrations.factories import AccessControlServiceBuilder


async def user_wrapper(user_id: int, token: str):
    try:
        access_control_service = AccessControlServiceBuilder.build_service(
            settings
        )

        await access_control_service.verify_token(user_id, token)

    except Exception as ex:
        raise HTTPException(400, "Bad request")
