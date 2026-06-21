#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from typing import Any
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = "Mission helper"
    OFFICER = "Engineering"
    LIEUTENANT = "Navigation"
    CAPTAIN = "Captain boss"
    COMMANDER = "Mission command"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=2, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_event_constraints(self) -> BaseModel:
        if not self.mission_id.startswith("M"):
            raise ValueError("Contact ID must start with 'M'")
        has_leader = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                has_leader = True
                break
        if not has_leader:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")
        if self.duration_days > 365:
            experienced_crew = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_crew += 1
            total = len(self.crew)
            if experienced_crew < total / 2:
                raise ValueError("Long missions require "
                                 " at least 50% experienced crew")
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def create_mission(data: dict[str, Any]) -> SpaceMission | None:
    try:
        return SpaceMission(**data)
    except ValidationError as e:
        print("=" * 40)
        print("Space mission creation aborted!")
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"], end="\n\n")
        return None


def report(mission: SpaceMission) -> None:
    try:
        print("Space Mission Crew Validation")
        print("=" * 40)
        print("Valid mission created:\n"
              f"Mission: {mission.mission_name}\n"
              f"ID: {mission.mission_id}\n"
              f"Destination: {mission.destination}\n"
              f"Budget: ${mission.budget_millions}M\n"
              f"Crew size: {len(mission.crew)}\n"
              f"Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.name.lower()}) - "
                  f"{member.rank.value} * "
                  f"{member.specialization}")
    except Exception as e:
        print(f"ERROR ON REPORT(): {e}")


if __name__ == '__main__':
    # Ok mission
    mission_data = {
        "mission_id": "M2026_ARRAKIS",
        "mission_name": "Exchange of fiefdom over Arrakis",
        "destination": "Arrakis",
        "launch_date": "5026-06-21",
        "duration_days": 900,
        "budget_millions": 250.0,
        "crew": [
            {
                "member_id": "C001",
                "name": "Leto Atreides",
                "rank": Rank.COMMANDER,
                "age": 45,
                "specialization": "Duke of Great House Atreides",
                "years_experience": 20,
                "is_active": True
            },
            {
                "member_id": "C002",
                "name": "Gurney Halleck",
                "rank": Rank.LIEUTENANT,
                "age": 35,
                "specialization": "Warmaster",
                "years_experience": 10,
                "is_active": True
            },
            {
                "member_id": "C003",
                "name": "Wellington Yueh",
                "rank": Rank.OFFICER,
                "age": 30,
                "specialization": "Suk Doctor",
                "years_experience": 8,
                "is_active": True
            }
        ]
    }
    mission = create_mission(mission_data)
    if isinstance(mission, SpaceMission):
        report(mission)

    f_mission_data = {
        "mission_id": "M2026_FAIL",
        "mission_name": "Musk's Mars Colony",
        "destination": "Mars",
        "launch_date": "2026-01-01",
        "duration_days": 900,
        "budget_millions": 10000.0,
        "crew": [
            {
                "member_id": "C001",
                "name": "Elon Musk",
                "rank": Rank.CADET,
                "age": 35,
                "specialization": "Government Efficiency",
                "years_experience": 1,
                "is_active": True
            }
        ]
    }
    f_mission = create_mission(f_mission_data)
    if isinstance(f_mission, SpaceMission):
        report(f_mission)
