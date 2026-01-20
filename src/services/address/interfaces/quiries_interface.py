from abc import ABC, abstractmethod
from typing import List

from schemas.adderess import AddressValidationRequest
from schemas.adderess import AddressRecognitionRequest


class AddressValidationQueriesInterface(ABC):

    @abstractmethod
    async def validate(
        self,
        addresses: List[AddressValidationRequest]
    ) -> List[dict]:
        pass

    @abstractmethod
    async def recognize(
            self,
            request: AddressRecognitionRequest
    ) -> dict:
        pass