from sqlalchemy import Column, String, Enum as SQLEnum, DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

from database.base import Base


class AddressStatus(str, enum.Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    WARNING = "warning"
    ERROR = "error"


class ResidentialIndicator(str, enum.Enum):
    UNKNOWN = "unknown"
    YES = "yes"
    NO = "no"


class Address(Base):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    company_name = Column(String(255), nullable=True)

    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255), nullable=True)
    address_line3 = Column(String(255), nullable=True)
    city_locality = Column(String(100), nullable=False)
    state_province = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=True)
    country_code = Column(String(2), nullable=False)
    address_residential_indicator = Column(
        SQLEnum(ResidentialIndicator),
        default=ResidentialIndicator.UNKNOWN,
        nullable=False
    )

    matched_address_line1 = Column(String(255), nullable=True)
    matched_address_line2 = Column(String(255), nullable=True)
    matched_address_line3 = Column(String(255), nullable=True)
    matched_city_locality = Column(String(100), nullable=True)
    matched_state_province = Column(String(100), nullable=True)
    matched_postal_code = Column(String(20), nullable=True)
    matched_country_code = Column(String(2), nullable=True)

    status = Column(
        SQLEnum(AddressStatus),
        default=AddressStatus.UNVERIFIED,
        nullable=False
    )

    validation_messages = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    def __repr__(self):
        return f"<Address(id={self.id}, status={self.status})>"