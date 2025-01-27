from abc import ABC, abstractmethod
from typing import Any

from typing_extensions import Unpack


class IBaseIMEICheckAPI(ABC):
    @abstractmethod
    async def check(self, *args: Unpack[Any], **kwargs: Any) -> dict[Any, Any]:
        raise NotImplementedError
