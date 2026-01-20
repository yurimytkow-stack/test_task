from sqlalchemy.ext.asyncio import AsyncSession

from models.address import Address
from services.address.interfaces.address_repository_interfaces import AddressRepositoryInterface

class AddressRepository(AddressRepositoryInterface):

    async def create(self, address_data: dict, session: AsyncSession) -> Address:
        clean_data = {k: v for k, v in address_data.items() if not k.startswith('_')}

        address = Address(**clean_data)
        session.add(address)
        await session.flush()
        await session.refresh(address)
        return address