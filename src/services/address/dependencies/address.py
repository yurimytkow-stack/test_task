from services.address.address_factories.address_factories import AddressFactory
from services.address.address_repository.address_repository import AddressRepository
from services.address.address_service import AddressService
from services.address.interfaces.address_service_interfaces import AddressServiceInterface
from services.address.quiries.quiries import AddressValidationQueries


def get_address_service() -> AddressServiceInterface:

    address_repository = AddressRepository()
    address_factory = AddressFactory()
    validation_queries = AddressValidationQueries()

    return AddressService(
        address_repository=address_repository,
        address_factory=address_factory,
        validation_queries=validation_queries
    )