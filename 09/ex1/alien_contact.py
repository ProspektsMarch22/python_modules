#!/usr/bin/env python3

# Refer to ex0 for env details

from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from typing import Optional, Any
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    VISUAL = "visual"
    RADIO = "radio"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=300)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_event(self) -> BaseModel:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")
        return self


def create_contact(data: dict[str, Any]) -> AlienContact | None:
    try:
        return AlienContact(**data)
    except ValidationError as e:
        print("=" * 40)
        print("Alien Contact Log creation aborted!")
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"], end="\n\n")
        return None


def report(contact: AlienContact) -> None:
    try:
        print("Alien Contact Log Validation")
        print("=" * 40)
        print("Valid contact report:\n"
              f"ID: {contact.contact_id}\n"
              f"Type: {contact.contact_type}\n"
              f"Location: {contact.location}\n"
              f"Signal: {contact.signal_strength}/10\n"
              f"Duration: {contact.duration_minutes} minutes\n"
              f"witnesses: {contact.witness_count}\n")
        if contact.message_received:
            print(f"Message: '{contact.message_received}'\n")
    except Exception as e:
        print(f"ERROR ON REPORT(): {e}")


if __name__ == '__main__':
    # Ok contact
    contact_data = {
        "contact_id": "AC_BILU_001",
        "timestamp": "2026-06-21",
        "contact_type": ContactType.PHYSICAL,
        "location": "Zigurats, Corguinho, MS",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 3,
        "message_received": "Apenas que busquem conhecimento!",
        "is_verified": True
    }
    ok_contact = create_contact(contact_data)
    if isinstance(ok_contact, AlienContact):
        report(ok_contact)

    # Not ok contact
    failed_contact = {
        "contact_id": "DC_2026_001",
        "timestamp": datetime(2026, 6, 21, 0, 0),
        "contact_type": ContactType.TELEPATHIC,
        "location": "Campo Largo, PR",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 1
    }
    f_contact = create_contact(failed_contact)
    if isinstance(f_contact, AlienContact):
        report(f_contact)
