import json
from typing import List, Optional, Dict, Union
from pydantic import BaseModel, Field


# Represents a feature at a specific level (e.g., Rage)
class Spell(BaseModel):
    name: str
    school: str
    tier: str
    casting_time: str
    description: str
    target: Optional[str] = None
    concentration: Optional[str] = None
    spell_range: Optional[str] = None
    reaction: Optional[str] = None
    damage: Optional[str] = None
    notes: Optional[str] = None
    high_levels: Optional[str] = None
    upcast: Optional[str] = None


# Top level container for the entire JSON
class SpellDatabase(BaseModel):
    spells: List[Spell]


def load_game_data(filepath: str) -> SpellDatabase:
    # Explicitly use utf-8 to avoid Character Map errors
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # If the JSON is a list, wrap it so it matches the SpellDatabase model
    if isinstance(data, list):
        data = {"spells": data}

    # This single line converts the entire dictionary tree into nested objects
    return SpellDatabase.model_validate(data)


# Example Usage
spell_data = load_game_data("spells.json")
