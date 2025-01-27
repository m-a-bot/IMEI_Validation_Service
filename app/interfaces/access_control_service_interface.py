from abc import ABC, abstractmethod
from typing import Any

from typing_extensions import Unpack


class IAccessControlService(ABC):
    @abstractmethod
    async def verify_token(
        self, *args: Unpack[Any], **kwargs: Any
    ) -> dict[Any, Any]:
        raise NotImplementedError
