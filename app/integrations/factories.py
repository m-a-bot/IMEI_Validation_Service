from app.config import Settings
from app.integrations.access_control_service import AccessControlService
from app.integrations.imeicheck_net_api import IMEICheckNetAPI
from app.interfaces.imei_check_api_interface import IBaseIMEICheckAPI
from app.stubs.access_control_service_stub import AccessControlServiceStub


class IMEICheckAPIBuilder:
    @staticmethod
    def build_service(
        imei_api_name: str, settings: Settings
    ) -> IBaseIMEICheckAPI:
        if imei_api_name == "imeicheck.net":
            if settings.USE_SANDBOX:
                token = settings.IMEICHECK_TOKEN_SANDBOX
            else:
                token = settings.IMEICHECK_TOKEN_LIVE
            return IMEICheckNetAPI(
                service_url=settings.IMEICHECK_VALIDATION_URL,
                service_token=token,
            )


class AccessControlServiceBuilder:
    @staticmethod
    def build_service(settings: Settings):
        if settings.VERIFY_TOKEN_URL in "test":
            return AccessControlServiceStub(settings.VERIFY_TOKEN_URL)
        else:
            return AccessControlService(settings.VERIFY_TOKEN_URL)
