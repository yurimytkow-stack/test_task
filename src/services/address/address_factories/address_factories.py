from models.address import Address, AddressStatus
from schemas.adderess import AddressValidationRequest
from services.address.interfaces.address_factories_interfaces import AddressFactoryInterface


class AddressFactory(AddressFactoryInterface):

    def create_address(
            self,
            address_request: AddressValidationRequest,
            matched_address: dict = None,
            status: str = "unverified",
            validation_messages: str = None
    ) -> Address:

        address_data = {
            "name": address_request.name,
            "phone": address_request.phone,
            "email": address_request.email,
            "company_name": address_request.company_name,

            "address_line1": address_request.address_line1,
            "address_line2": address_request.address_line2,
            "address_line3": address_request.address_line3,
            "city_locality": address_request.city_locality,
            "state_province": address_request.state_province,
            "postal_code": address_request.postal_code,
            "country_code": address_request.country_code,
            "address_residential_indicator": address_request.address_residential_indicator,

            "status": AddressStatus(status),
            "validation_messages": validation_messages
        }

        if matched_address:
            address_data.update({
                "matched_address_line1": matched_address.get("address_line1"),
                "matched_address_line2": matched_address.get("address_line2"),
                "matched_address_line3": matched_address.get("address_line3"),
                "matched_city_locality": matched_address.get("city_locality"),
                "matched_state_province": matched_address.get("state_province"),
                "matched_postal_code": matched_address.get("postal_code"),
                "matched_country_code": matched_address.get("country_code")
            })

        return Address(**address_data)