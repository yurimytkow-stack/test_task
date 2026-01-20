from typing import List

from schemas.adderess import AddressValidationRequest, AddressRecognitionRequest
from services.address.interfaces.quiries_interface import AddressValidationQueriesInterface



class AddressValidationQueries(AddressValidationQueriesInterface):

    async def validate(
            self,
            addresses: List[AddressValidationRequest]
    ) -> List[dict]:

        results = []
        for address in addresses:
            results.append({
                "status": "verified",
                "original_address": address.model_dump(exclude_none=True),
                "matched_address": {
                    "address_line1": address.address_line1,
                    "address_line2": address.address_line2,
                    "address_line3": address.address_line3,
                    "city_locality": address.city_locality,
                    "state_province": address.state_province,
                    "postal_code": address.postal_code,
                    "country_code": address.country_code
                },
                "messages": []
            })

        return results

    async def recognize(
            self,
            request: AddressRecognitionRequest
    ) -> dict:
        return {
            "score": 0.91,
            "address": {
                "name": "John Doe",
                "address_line1": "123 Main St",
                "address_line2": "Apt 4B",
                "city_locality": "Kyiv",
                "state_province": "Kyivska",
                "postal_code": "01001",
                "address_residential_indicator": "unknown"
            },
            "entities": [
                {
                    "type": "person",
                    "score": 0.95,
                    "text": "John Doe",
                    "start_index": 0,
                    "end_index": 8,
                    "result": {}
                },
                {
                    "type": "address_line",
                    "score": 0.98,
                    "text": "123 Main St",
                    "start_index": 12,
                    "end_index": 23,
                    "result": {}
                },
                {
                    "type": "city_locality",
                    "score": 0.96,
                    "text": "Kyiv",
                    "start_index": 32,
                    "end_index": 36,
                    "result": {}
                }
            ]
        }