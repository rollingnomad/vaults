import json
from typing import List, Optional, Dict, Union
from pydantic import BaseModel, Field


# Represents a feature at a specific level (e.g., Rage)
class Feat(BaseModel):
    name: str
    text: str


class Ancestry(BaseModel):
    name: str
    rarity: str
    size: str
    description: str
    trait: Feat


# Top level container for the entire JSON
class AncestryDatabase(BaseModel):
    ancestries: List[Ancestry]


def load_game_data(filepath: str) -> AncestryDatabase:
    # Explicitly use utf-8 to avoid Character Map errors
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # This single line converts the entire dictionary tree into nested objects
    return AncestryDatabase.model_validate(data)


# Example Usage
ancestry_data = load_game_data("ancestries.json")
