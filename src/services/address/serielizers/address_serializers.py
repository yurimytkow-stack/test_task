import json
from typing import List, Optional

from models.address import Address
from response_schemas.address import AddressValidationResponse
from schemas.adderess import (
    OriginalAddress,
    MatchedAddress,
    ValidationMessage
)


class AddressSerializer:

    def serialize_validation_response(
            self,
            address: Address,
            validation_result: dict
    ) -> AddressValidationResponse:

        original_address = self._serialize_original_address(address)
        matched_address = self._serialize_matched_address(address)
        messages = self._serialize_messages(address.validation_messages)

        return AddressValidationResponse(
            status=address.status.value,
            original_address=original_address,
            matched_address=matched_address,
            messages=messages
        )

    def _serialize_original_address(self, address: Address) -> OriginalAddress:
        return OriginalAddress(
            name=address.name,
            phone=address.phone,
            email=address.email,
            company_name=address.company_name,
            address_line1=address.address_line1,
            address_line2=address.address_line2,
            address_line3=address.address_line3,
            city_locality=address.city_locality,
            state_province=address.state_province,
            postal_code=address.postal_code,
            country_code=address.country_code,
            address_residential_indicator=address.address_residential_indicator.value
        )

    def _serialize_matched_address(self, address: Address) -> Optional[MatchedAddress]:
        if not address.matched_address_line1:
            return None

        return MatchedAddress(
            address_line1=address.matched_address_line1,
            address_line2=address.matched_address_line2,
            address_line3=address.matched_address_line3,
            city_locality=address.matched_city_locality,
            state_province=address.matched_state_province,
            postal_code=address.matched_postal_code,
            country_code=address.matched_country_code
        )

    def _serialize_messages(
            self,
            validation_messages_json: Optional[str]
    ) -> List[ValidationMessage]:
        if not validation_messages_json:
            return []

        try:
            messages_data = json.loads(validation_messages_json)
            return [
                ValidationMessage(
                    code=msg.get("code"),
                    message=msg.get("message"),
                    type=msg.get("type"),
                    detail_code=msg.get("detail_code")
                )
                for msg in messages_data
            ]
        except (json.JSONDecodeError, TypeError):
            return []