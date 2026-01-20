from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from models.address import Address



class AddressRepositoryInterface(ABC):

    @abstractmethod
    async def create(self, address_data: dict, session: AsyncSession) -> Address:
        pass