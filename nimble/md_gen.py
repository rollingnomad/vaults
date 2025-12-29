import os
import re
from jinja2 import Environment, FileSystemLoader
from job_json_to_obj import class_data
from anc_json_to_obj import ancestry_data
from spells_json_to_obj import spell_data


def clean_table_text(value):
    if not value:
        return ""
    # Tables must be one physical line: convert \n to spaces so they don't break the cell
    return str(value).replace("\n", " ").replace("|", r"\|")


def format_paragraphs(value):
    if not value:
        return ""
    # 1. Normalize any existing multiple newlines to double newlines
    text = re.sub(r"\n{2,}", "\n\n", str(value))
    # 2. Convert single newlines to double newlines (Markdown's paragraph requirement)
    # This prevents the "blob" effect.
    return text.replace("\n", "\n\n")


def generate_markdown():
    env = Environment(loader=FileSystemLoader("templates"))
    env.filters["clean_table"] = clean_table_text
    env.filters["paragraphs"] = format_paragraphs

    # --- GENERATE CLASS PAGES ---
    class_template = env.get_template("class_page.md.j2")
    output_dir = "docs/classes"
    os.makedirs(output_dir, exist_ok=True)

    for char_class in class_data.classes:
        output_content = class_template.render(**char_class.model_dump())
        filename = f"{char_class.name.lower().replace(' ', '_')}.md"
        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
            f.write(output_content)

    # --- GENERATE ANCESTRY PAGE (Single File) ---
    ancestry_template = env.get_template("ancestry_page.md.j2")
    ancestry_output = ancestry_template.render(**ancestry_data.model_dump())

    with open("docs/ancestries.md", "w", encoding="utf-8") as f:
        f.write(ancestry_output)

    # --- GENERATE WELCOME (INDEX) PAGE ---
    index_template = env.get_template("index.md.j2")
    # Pass the whole list of classes to the index template
    index_content = index_template.render(classes=class_data.classes)

    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write(index_content)

    print("Generated: docs/index.md and all class pages.")

    # --- GENERATE INDIVIDUAL SPELL PAGES ---
    spell_output_dir = "docs/spells"
    os.makedirs(spell_output_dir, exist_ok=True)

    # 1. Group spells by school
    # This assumes school is now "Fire", "Ice", "Lightning", etc.
    grouped_spells = {}
    for spell in spell_data.spells:
        if spell.school not in grouped_spells:
            grouped_spells[spell.school] = []
        grouped_spells[spell.school].append(spell)

    # 2. Get the template
    try:
        school_template = env.get_template("spells_page.md.j2")
    except Exception as e:
        print(f"Error: Could not find school_page.md.j2 in templates folder. {e}")
        return

    # 3. Iterate through each school and create the file
    for school, spells in grouped_spells.items():
        # This converts "Fire" to "fire_spells.md"
        # and "Lightning" to "lightning_spells.md"
        clean_name = school.lower().strip().replace(" ", "_")
        filename = f"{clean_name}_spells.md"

        # Path: docs/spells/fire_spells.md
        file_path = os.path.join(spell_output_dir, filename)

        # Render the template
        output_content = school_template.render(school=school, spells=spells)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output_content)

        print(f"Generated: {file_path}")

    print(f"Successfully generated {len(grouped_spells)} school files.")


if __name__ == "__main__":
    generate_markdown()
