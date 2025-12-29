import json
from typing import List, Optional, Dict, Union
from pydantic import BaseModel, Field


# Represents a feature at a specific level (e.g., Rage)
class Feat(BaseModel):
    level: Optional[int] = None
    name: str
    text: str
    usage: Optional[str] = None
    action: Optional[str] = None


# Represents a subclass (e.g., Path of the Red Mist)
class Subclass(BaseModel):
    id: str
    name: str
    subclass_feats: List[Feat]


# The main Class model (Berserker, Mage, etc.)
class CharacterClass(BaseModel):
    name: str
    description: str
    key_stats: List[str]
    secondary_stats: List[str]
    hit_die: str
    starting_hp: int
    saves: Dict[str, List[str]]
    armor: str
    # Polymorphic field: can be a string ("All STR weapons") or a list (["Staff", "Wands"])
    weapons: Union[str, List[str]]
    starting_gear: List[str]
    level_feats: List[Feat]
    # Dict where key is the Arsenal name and value is a list of Feats
    class_feats: Dict[str, List[Feat]]
    subclasses: List[Subclass]


# Top level container for the entire JSON
class GameDatabase(BaseModel):
    classes: List[CharacterClass]


def load_game_data(filepath: str) -> GameDatabase:
    # Explicitly use utf-8 to avoid Character Map errors
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # This single line converts the entire dictionary tree into nested objects
    return GameDatabase.model_validate(data)


# Example Usage
class_data = load_game_data("heroes.json")
