with open("eb_full.md", "r", encoding="utf-8") as f:
    content = f.readlines()
    lines = [l.strip() for l in content]

processed_lines = []

for line in lines:
    if line.startswith("#"):
        hash_count = line.count("#")
        content = line.replace("#", "")

        new_content = content.upper()

        hashes = "#" * hash_count
        processed_lines.append(f"{hashes} {new_content}")

    else:
        processed_lines.append(line)


headings = [i for i in processed_lines if i.startswith("#")]

print(headings)


with open("edited_eb_full.md", "w", encoding="utf-8") as outfile:
    outfile.writelines(processed_lines)

print(f"Saved to {outfile}")
