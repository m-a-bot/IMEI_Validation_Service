from fastapi import APIRouter, Depends, Query

from app.access_control import user_wrapper
from app.config import settings
from app.schemes.pyd import IMEICheck
from app.services.check_imei_service import CheckIMEIService

check_imei_router = APIRouter(
    tags=["check_imei_router"], dependencies=[Depends(user_wrapper)]
)


@check_imei_router.post(
    "/api/check-imei",
)
async def check_imei(
    imei_check: IMEICheck,
    token: str = Query(...),
    user_id: int = Query(...),
):
    """Check imei"""
    return await CheckIMEIService(imei_api_name=settings.IMEI_API_NAME).check(
        imei_check
    )
