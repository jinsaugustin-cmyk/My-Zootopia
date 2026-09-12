import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts one animal object into HTML."""
    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += (
            f'<div class="card__title">{animal_obj["name"]}</div>\n'
        )

    output += '<div class="card__text">\n'
    output += '<ul class="card__details">\n'

    if "diet" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Diet:</strong> '
            f'{animal_obj["characteristics"]["diet"]}'
            f'</li>\n'
        )

    if "locations" in animal_obj and animal_obj["locations"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Location:</strong> '
            f'{animal_obj["locations"][0]}'
            f'</li>\n'
        )

    if "type" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Type:</strong> '
            f'{animal_obj["characteristics"]["type"]}'
            f'</li>\n'
        )

    if "lifespan" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Lifespan:</strong> '
            f'{animal_obj["characteristics"]["lifespan"]}'
            f'</li>\n'
        )

    if "weight" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Weight:</strong> '
            f'{animal_obj["characteristics"]["weight"]}'
            f'</li>\n'
        )

    if "skin_type" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Skin Type:</strong> '
            f'{animal_obj["characteristics"]["skin_type"]}'
            f'</li>\n'
        )

    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"

    return output


# Load animal data
animals_data = load_data("animals_data.json")


# >>> NEW: Create a set for unique skin types
skin_types = set()


# >>> NEW: Collect available skin types
for animal_obj in animals_data:
    characteristics = animal_obj.get("characteristics", {})

    if "skin_type" in characteristics:
        skin_types.add(characteristics["skin_type"])


# >>> NEW: Display available skin types
print("Available skin types:")

for skin_type in sorted(skin_types):
    print(skin_type)


# >>> NEW: Ask the user for a skin type
selected_skin_type = input("Enter a skin type: ")


# Generate HTML
output = ""

for animal_obj in animals_data:

    # >>> NEW: Get characteristics safely
    characteristics = animal_obj.get("characteristics", {})

    # >>> NEW: Only serialize matching animals
    if characteristics.get("skin_type") == selected_skin_type:
        output += serialize_animal(animal_obj)


# Optional temporary check
print(output)


# Read HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()


# Replace placeholder with animal HTML
new_html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output,
)


# Write final HTML file
with open("animals.html", "w") as file:
    file.write(new_html)