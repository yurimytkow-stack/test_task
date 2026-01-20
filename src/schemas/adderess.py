from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, EmailStr

from models.address import ResidentialIndicator


class AddressValidationRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=1, description="Contact person name")
    phone: Optional[str] = Field(None, min_length=1, description="Phone number")
    email: Optional[EmailStr] = Field(None, description="Email address")
    company_name: Optional[str] = Field(None, min_length=1, description="Company name")
    address_line1: str = Field(..., min_length=1, description="Address line 1")
    address_line2: Optional[str] = Field(None, min_length=1, description="Address line 2")
    address_line3: Optional[str] = Field(None, min_length=1, description="Address line 3")
    city_locality: str = Field(..., min_length=1, description="City or locality")
    state_province: str = Field(..., min_length=1, description="State or province")
    postal_code: Optional[str] = Field(None, min_length=1, description="Postal code")
    country_code: str = Field(..., min_length=2, max_length=2, description="Two-letter country code")
    address_residential_indicator: ResidentialIndicator = Field(
        default=ResidentialIndicator.UNKNOWN,
        description="Residential address indicator"
    )

    @field_validator('country_code')
    @classmethod
    def validate_country_code(cls, v: str) -> str:
        return v.upper()


class OriginalAddress(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    company_name: Optional[str] = None
    address_line1: str
    address_line2: Optional[str] = None
    address_line3: Optional[str] = None
    city_locality: str
    state_province: str
    postal_code: Optional[str] = None
    country_code: str
    address_residential_indicator: str


class MatchedAddress(BaseModel):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_line3: Optional[str] = None
    city_locality: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None


class ValidationMessage(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None
    type: Optional[str] = None
    detail_code: Optional[str] = None

class PartialAddress(BaseModel):
    name: Optional[str] = None
    company_name: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_line3: Optional[str] = None
    city_locality: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None


class AddressRecognitionRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Unstructured text containing address")
    address: Optional[PartialAddress] = Field(None, description="Already known address values")


class RecognizedEntity(BaseModel):
    type: str = Field(..., description="Entity type (person, address_line, city_locality, etc.)")
    score: float = Field(..., ge=0, le=1, description="Confidence score")
    text: str = Field(..., description="Original text")
    start_index: int = Field(..., description="Start position in text")
    end_index: int = Field(..., description="End position in text")
    result: dict = Field(default_factory=dict, description="Additional result data")


class ParsedAddress(BaseModel):
    name: Optional[str] = None
    company_name: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_line3: Optional[str] = None
    city_locality: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    address_residential_indicator: str = "unknown"