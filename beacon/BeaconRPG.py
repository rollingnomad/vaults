from typing import List, Dict, Optional, Callable
import csv
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Ability:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    size: str
    weapon_type: str
    memory: str
    tags: List[str]
    action: str
    ability_range: str
    damage: str
    text: str
    rarity: str
    hp: int
    recoveries: int
    dodge: int
    speed: int
    memory_increase: int
    stresscap: int
    a_def: int
    mp: int
    armor: int
    save_target: int
    scope: int
    size_2: int

    def to_spell(self):
        return Spell(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            memory=self.memory,
            tags=self.tags,
            action=self.action,
            damage=self.damage,
            ability_range=self.ability_range,
            text=self.text,
        )

    def to_skill(self):
        return Skill(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            memory=self.memory,
            tags=self.tags,
            action=self.action,
            damage=self.damage,
            ability_range=self.ability_range,
            text=self.text,
        )

    def to_weapon(self):
        return Weapon(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            size=self.size,
            weapon_type=self.weapon_type,
            tags=self.tags,
            action=self.action,
            damage=self.damage,
            ability_range=self.ability_range,
            text=self.text,
        )

    def to_limitbreak(self):
        return LimitBreak(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            tags=self.tags,
            action=self.action,
            ability_range=self.ability_range,
            text=self.text,
        )

    def to_talent(self):
        return Talent(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            rank=self.specific_ability_type.replace("Rank ", ""),
            text=self.text,
        )

    def to_trait(self):
        return Trait(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            tags=self.tags,
            action=self.action,
            ability_range=self.ability_range,
            text=self.text,
        )

    def to_supportitem(self):
        return SupportItem(
            origin=self.origin,
            name=self.name,
            job_rank=self.job_rank,
            ability_type=self.ability_type,
            specific_ability_type=self.specific_ability_type,
            size=self.size,
            tags=self.tags,
            action=self.action,
            ability_range=self.ability_range,
            text=self.text,
            dodge=self.dodge,
            speed=self.speed,
            armor=self.armor,
            save_target=self.save_target,
        )


# Dark Blue
@dataclass
class Weapon:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    size: str
    weapon_type: str
    tags: List[str]
    action: str
    ability_range: str
    damage: str
    text: str
    pass


# Light Blue
@dataclass
class Spell:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    memory: str
    tags: List[str]
    action: str
    ability_range: str
    damage: str
    text: str
    pass


# Brown
@dataclass
class SupportItem:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    size: str
    tags: List[str]
    action: str
    ability_range: str
    dodge: str
    speed: str
    armor: str
    text: str
    save_target: str


# Orange
@dataclass
class Trait:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    tags: List[str]
    action: str
    ability_range: str
    text: str
    pass


# Teal
@dataclass
class Skill:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    memory: str
    tags: List[str]
    action: str
    ability_range: str
    damage: str
    text: str
    pass


# Pink
@dataclass
class LimitBreak:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    specific_ability_type: str
    tags: List[str]
    action: str
    ability_range: str
    text: str
    pass


@dataclass
class Talent:
    origin: str
    name: str
    job_rank: str
    ability_type: str
    rank: str
    text: str
    pass


@dataclass
class Job:
    name: str
    scope: int
    hp: int
    recoveries: int
    dodge: int
    speed: int
    stresscap: int
    memory: int
    a_def: int
    mp: int
    save: int
    weapon_slots: list
    support_slots: list
    limitbreak: LimitBreak
    role: str
    spells: list
    skills: list
    limitbreaks: list
    weapons: list
    talents: list
    traits: list
    support_items: list
    pass


@dataclass
class Ancestry:
    pass


def get_all_abilities(filename="ability_index.csv") -> List:
    abilities = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tag_list = row["Tags"].split(",")
            abilities.append(
                Ability(
                    origin=row["Origin"],
                    name=row["Name"],
                    job_rank=row["Job Rank"],
                    ability_type=row["Ability Type"],
                    specific_ability_type=row["Specific Ability Type"],
                    size=row["Size"],
                    weapon_type=row["Type"],
                    memory=row["Memory"],
                    tags=tag_list,
                    action=row["Action"],
                    ability_range=row["Range"].replace("[", "").replace("]", ""),
                    damage=row["Damage"]
                    .replace("-", "")
                    .replace("[", "")
                    .replace("]", ""),
                    text=row["Text"],
                    rarity=row["Rarity"].capitalize(),
                    hp=int(row["HP"] or 0),
                    recoveries=int(row["Recoveries"] or 0),
                    dodge=int(row["Dodge"] or 0),
                    speed=int(row["Speed"] or 0),
                    memory_increase=int(row["Memory Increase"] or 0),
                    stresscap=int(row["Stresscap"] or 0),
                    a_def=int(row["A-Def"] or 0),
                    mp=int(row["MP"] or 0),
                    armor=int(row["Armor"] or 0),
                    save_target=int(row["Save Target"] or 0),
                    scope=int(row["Scope"] or 0),
                    size_2=str(row["Size"] or 0),
                )
            )

    return abilities


raw_abilities = get_all_abilities()


# def get_objs(raw_abilities: List):
#     spells = [a.to_spell() for a in raw_abilities if a.ability_type.lower() == "spell"]
#     skills = [a.to_skill() for a in raw_abilities if a.ability_type.lower() == "skill"]
#     limitbreaks = [
#         a.to_limitbreak()
#         for a in raw_abilities
#         if a.ability_type.lower() == "limit break"
#     ]
#     weapons = [
#         a.to_weapon() for a in raw_abilities if a.ability_type.lower() == "weapon"
#     ]
#     talents = [
#         a.to_talent() for a in raw_abilities if a.ability_type.lower() == "talent"
#     ]
#     traits = [a.to_trait() for a in raw_abilities if a.ability_type.lower() == "trait"]
#     support_items = [
#         a.to_supportitem() for a in raw_abilities if a.ability_type.lower() == "support"
#     ]

#     return spells, skills, limitbreaks, weapons, talents, traits, support_items


ABILITY_BUILDERS: dict[str, Callable[[Ability], object]] = {
    "spell": Ability.to_spell,
    "skill": Ability.to_skill,
    "limit break": Ability.to_limitbreak,
    "weapon": Ability.to_weapon,
    "talent": Ability.to_talent,
    "trait": Ability.to_trait,
    "support": Ability.to_supportitem,
}


def build_abilities(raw_abilities: list[Ability]) -> dict[str, list]:
    buckets = defaultdict(list)

    for ability in raw_abilities:
        key = ability.ability_type.lower()
        builder = ABILITY_BUILDERS.get(key)
        if builder:
            buckets[key].append(builder(ability))

    return buckets


abilities_by_type = build_abilities(raw_abilities)

spells = abilities_by_type["spell"]
skills = abilities_by_type["skill"]
limitbreaks = abilities_by_type["limit break"]
weapons = abilities_by_type["weapon"]
talents = abilities_by_type["talent"]
traits = abilities_by_type["trait"]
support_items = abilities_by_type["support"]


def index_by_name(items):
    return {item.name: item for item in items}


spell_by_name = index_by_name(spells)
skill_by_name = index_by_name(skills)
limitbreak_by_name = index_by_name(limitbreaks)
weapon_by_name = index_by_name(weapons)
talent_by_name = index_by_name(talents)
trait_by_name = index_by_name(traits)
support_item_by_name = index_by_name(support_items)

all_abilities = (
    spells + skills + limitbreaks + weapons + talents + traits + support_items
)


def group_by_origin(abilities):
    grouped = defaultdict(list)
    for a in abilities:
        grouped[a.origin.lower()].append(a)
    return grouped


abilities_by_origin = group_by_origin(all_abilities)


def non_empty(*values):
    return [v for v in values if v]


def resolve_traits(*names):
    return [trait_by_name[name] for name in names if name]


def get_jobs(filename: str = "jobs.csv"):
    jobs: dict[str, Job] = {}
    with open("jobs.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Job"]
            job_abilities = abilities_by_origin[name.lower()]
            job = Job(
                name=name,
                scope=int(row["Scope"]),
                hp=int(row["HP"]),
                recoveries=int(row["Recoveries"]),
                dodge=int(row["Dodge"]),
                speed=int(row["Speed"]),
                stresscap=int(row["Stress_Cap"]),
                memory=int(row["Memory"]),
                a_def=int(row["A_Def"]),
                mp=int(row["MP"]),
                save=int(row["Save"]),
                weapon_slots=non_empty(
                    row["Weapon_Slot_1"],
                    row["Weapon_Slot_2"],
                    row["Weapon_Slot_3"],
                ),
                support_slots=non_empty(
                    row["Support_Slot_1"],
                    row["Support_Slot_2"],
                    row["Support_Slot_3"],
                    row["Support_Slot_4"],
                ),
                limitbreak=limitbreak_by_name.get(row["Limit_Break"]),
                role=row["Role"],
                spells=[a for a in job_abilities if isinstance(a, Spell)],
                skills=[a for a in job_abilities if isinstance(a, Skill)],
                limitbreaks=[a for a in job_abilities if isinstance(a, LimitBreak)],
                weapons=[a for a in job_abilities if isinstance(a, Weapon)],
                talents=[a for a in job_abilities if isinstance(a, Talent)],
                traits=[a for a in job_abilities if isinstance(a, Trait)],
                support_items=[a for a in job_abilities if isinstance(a, SupportItem)],
            )

            jobs[name] = job

    return jobs


jobs = get_jobs()

# ////////////////////

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=False,
)

template = env.get_template("job.md.j2")

DOCS_DIR = Path("docs/jobs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")


def generate_job_docs(jobs: dict[str, Job]) -> None:
    for job in jobs.values():
        content = template.render(job=job).strip() + "\n"
        filepath = DOCS_DIR / f"{slugify(job.name)}.md"
        filepath.write_text(content, encoding="utf-8")
        print(f"Generated {filepath}")


generate_job_docs(jobs)

# ////////////////////
