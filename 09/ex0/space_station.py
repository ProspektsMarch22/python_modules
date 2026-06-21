#!/usr/bin/env python3

# Its possible that pydantic is not installed. If not:
# python3 -m venv venv
# source venv/bin/activate
# pip install pydantic

from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Any
from datetime import datetime


class SpaceStation_Model(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def create_station(data: dict[str, Any]) -> SpaceStation_Model | None:
    try:
        return SpaceStation_Model(**data)
    except ValidationError as e:
        print("=" * 40)
        print("Station creation aborted!")
        print("Expected validation error:")
        for err in e.errors():
            print(f"In field: {err["loc"][0]}")
            print(err["msg"], end="\n\n")
        return None


def report(station: SpaceStation_Model) -> None:
    try:
        print("Space Station Data Validation\n")
        print("=" * 40)
        print("Valid station created:\n"
              f"ID: {station.station_id}\n"
              f"Name: {station.name}\n"
              f"Crew: {station.crew_size} people\n"
              f"Power: {station.power_level}%\n"
              f"Last last_maintenance: {station.last_maintenance}\n"
              f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Not operational"
        print(f"Status: {status}\n")
    except Exception as e:
        print(f"ERROR ON REPORT(): {e}")


if __name__ == '__main__':
    # OK station
    station_data = {
        "station_id": "ISS001",
        "name": "International Space Station 1",
        "crew_size": 6,
        "power_level": 85.5,
        "last_maintenance": datetime(2026, 6, 21, 0, 0),
        "oxygen_level": 92.3,
        "notes": "Notes are working as well"
    }
    ok_station = create_station(station_data)
    if isinstance(ok_station, SpaceStation_Model):
        report(ok_station)

    # Not OK station
    failed_station = {
        "station_id": "ISS001",
        "name": "International Space Station 1",
        "crew_size": 100,
        "power_level": 101.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2026-06-21",
        "notes": "Notes are working as well"
    }
    f_station = create_station(failed_station)
    if isinstance(f_station, SpaceStation_Model):
        report(f_station)
