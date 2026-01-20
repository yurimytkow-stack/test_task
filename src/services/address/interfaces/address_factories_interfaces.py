from abc import ABC, abstractmethod

from models.address import Address
from schemas.adderess import AddressValidationRequest


class AddressFactoryInterface(ABC):

    @abstractmethod
    def create_address(
        self,
        address_request: AddressValidationRequest,
        matched_address: dict = None,
        status: str = "unverified",
        validation_messages: str = None
    ) -> Address:
        pass