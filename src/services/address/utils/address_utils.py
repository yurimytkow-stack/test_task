import json
from models.address import AddressStatus


class AddressUtils:

    @staticmethod
    def map_status(external_status: str) -> AddressStatus:
        status_map = {
            "verified": AddressStatus.VERIFIED,
            "warning": AddressStatus.WARNING,
            "error": AddressStatus.ERROR,
            "unverified": AddressStatus.UNVERIFIED
        }
        return status_map.get(external_status, AddressStatus.UNVERIFIED)

    @staticmethod
    def serialize_messages(messages: list) -> str:
        return json.dumps(messages) if messages else None