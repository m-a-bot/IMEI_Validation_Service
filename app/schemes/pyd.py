from typing import List, Literal

from pydantic import BaseModel, Field, ValidationError, model_validator
from stdnum.imei import is_valid
from typing_extensions import Self


class IMEICheck(BaseModel):
    deviceId: str = Field(...)
    serviceId: int = Field(...)

    @model_validator(mode="after")
    def check_deviceId_is_valid(self) -> Self:
        if not is_valid(self.deviceId):
            raise ValidationError("deviceId is not valid")
        return self

    class Config:
        json_schema_extra = {
            "example": {
                "deviceId": "123456789012345",
                "serviceId": 14,
            }
        }


class HTTPExceptionResponse(BaseModel):
    detail: str
