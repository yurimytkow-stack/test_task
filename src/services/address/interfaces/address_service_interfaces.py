from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from response_schemas.address import AddressValidationResponse
from schemas.adderess import AddressValidationRequest
from response_schemas.address import AddressRecognitionResponse
from schemas.adderess import AddressRecognitionRequest


class AddressServiceInterface(ABC):

    @abstractmethod
    async def validate_addresses(
        self,
        addresses: List[AddressValidationRequest],
        session: AsyncSession
    ) -> List[AddressValidationResponse]:
        pass

    @abstractmethod
    async def recognize_address(
            self,
            request: AddressRecognitionRequest
    ) -> AddressRecognitionResponse:
        pass