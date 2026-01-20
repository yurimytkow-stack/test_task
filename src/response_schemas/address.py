from typing import Optional, List
from pydantic import BaseModel, Field

from schemas.adderess import OriginalAddress, MatchedAddress, ValidationMessage, ParsedAddress, RecognizedEntity




class AddressValidationResponse(BaseModel):
    status: str = Field(..., description="Validation status: verified, warning, error, unverified")
    original_address: OriginalAddress
    matched_address: Optional[MatchedAddress] = None
    messages: List[ValidationMessage] = Field(default_factory=list)

class AddressRecognitionResponse(BaseModel):
    score: float = Field(..., ge=0, le=1, description="Overall confidence score")
    address: ParsedAddress = Field(..., description="Parsed address")
    entities: List[RecognizedEntity] = Field(default_factory=list, description="Recognized entities")