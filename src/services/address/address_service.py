from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from models.address import Address
from services.address.interfaces.address_factories_interfaces import AddressFactoryInterface
from services.address.interfaces.address_repository_interfaces import AddressRepositoryInterface
from services.address.interfaces.address_service_interfaces import AddressServiceInterface
from services.address.interfaces.quiries_interface import AddressValidationQueriesInterface
from services.address.serielizers.address_serializers import AddressSerializer
from services.address.utils.address_utils import AddressUtils
from response_schemas.address import AddressValidationResponse
from schemas.adderess import AddressValidationRequest
from response_schemas.address import AddressRecognitionResponse
from schemas.adderess import AddressRecognitionRequest


class AddressService(AddressServiceInterface):

    def __init__(
            self,
            address_repository: AddressRepositoryInterface,
            address_factory: AddressFactoryInterface,
            validation_queries: AddressValidationQueriesInterface
    ):
        self.address_repository = address_repository
        self.address_factory = address_factory
        self.validation_queries = validation_queries
        self.serializer = AddressSerializer()

    async def validate_addresses(
            self,
            addresses: List[AddressValidationRequest],
            session: AsyncSession
    ) -> List[AddressValidationResponse]:

        validation_results = await self.validation_queries.validate(addresses)

        responses = []
        for idx, validation_result in enumerate(validation_results):
            address = self._build_address(addresses[idx], validation_result)

            saved_address = await self.address_repository.create(
                address_data={k: v for k, v in address.__dict__.items() if not k.startswith('_')},
                session=session
            )

            response = self.serializer.serialize_validation_response(
                saved_address,
                validation_result
            )
            responses.append(response)

        return responses

    def _build_address(
            self,
            request: AddressValidationRequest,
            validation_result: dict
    ) -> Address:

        status = AddressUtils.map_status(validation_result.get("status", "unverified"))
        matched_address = validation_result.get("matched_address")
        messages = validation_result.get("messages", [])
        validation_messages = AddressUtils.serialize_messages(messages)

        return self.address_factory.create_address(
            address_request=request,
            matched_address=matched_address,
            status=status.value,
            validation_messages=validation_messages
        )

    async def recognize_address(
            self,
            request: AddressRecognitionRequest
    ) -> AddressRecognitionResponse:

        recognition_result = await self.validation_queries.recognize(request)

        return AddressRecognitionResponse(
            score=recognition_result.get("score", 0.0),
            address=recognition_result.get("address", {}),
            entities=recognition_result.get("entities", [])
        )