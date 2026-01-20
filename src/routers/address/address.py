from typing import List
from fastapi import Depends, APIRouter, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db
from response_schemas.address import AddressValidationResponse
from schemas.adderess import AddressValidationRequest
from services.address.dependencies.address import get_address_service
from services.address.interfaces.address_service_interfaces import AddressServiceInterface
from response_schemas.address import AddressRecognitionResponse
from schemas.adderess import AddressRecognitionRequest

router = APIRouter(prefix="/addresses")


@router.post("/validate", response_model=List[AddressValidationResponse], status_code=status.HTTP_200_OK)
async def validate_addresses(
        addresses: List[AddressValidationRequest],
        session: AsyncSession = Depends(get_db),
        address_service: AddressServiceInterface = Depends(get_address_service)
):
    try:
        results = await address_service.validate_addresses(addresses, session)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Address validation failed: {str(e)}"
        )

@router.put("/recognize", response_model=AddressRecognitionResponse, status_code=status.HTTP_200_OK)
async def recognize_address(
        request: AddressRecognitionRequest,
        address_service: AddressServiceInterface = Depends(get_address_service)
):
    try:
        result = await address_service.recognize_address(request)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Address recognition failed: {str(e)}"
        )