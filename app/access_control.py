import logging

from fastapi import HTTPException

from app.config import settings
from app.integrations.factories import AccessControlServiceBuilder


async def user_wrapper(user_id: int, token: str):
    try:
        access_control_service = AccessControlServiceBuilder.build_service(
            settings
        )

        await access_control_service.verify_token(user_id, token)

    except HTTPException as ex:
        raise ex

    except Exception as ex:

        logging.error(f"Unexpected error in user_wrapper: {ex}")

        raise HTTPException(500, "Internal Server Error") from ex
