import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts one animal object into HTML."""
    output = ""

    # Start animal card
    output += '<li class="cards__item">\n'

    # Animal name
    if "name" in animal_obj:
        output += (
            f'<div class="card__title">{animal_obj["name"]}</div>\n'
        )

    # Start animal details
    output += '<div class="card__text">\n'
    output += '<ul class="card__details">\n'

    # Diet
    if "diet" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Diet:</strong> '
            f'{animal_obj["characteristics"]["diet"]}'
            f'</li>\n'
        )

    # Location
    if "locations" in animal_obj and animal_obj["locations"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Location:</strong> '
            f'{animal_obj["locations"][0]}'
            f'</li>\n'
        )

    # Type
    if "type" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Type:</strong> '
            f'{animal_obj["characteristics"]["type"]}'
            f'</li>\n'
        )

    # Bonus: Lifespan
    if "lifespan" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Lifespan:</strong> '
            f'{animal_obj["characteristics"]["lifespan"]}'
            f'</li>\n'
        )

    # Bonus: Weight
    if "weight" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Weight:</strong> '
            f'{animal_obj["characteristics"]["weight"]}'
            f'</li>\n'
        )

    # Bonus: Skin Type
    if "skin_type" in animal_obj["characteristics"]:
        output += (
            f'<li class="card__detail">'
            f'<strong>Skin Type:</strong> '
            f'{animal_obj["characteristics"]["skin_type"]}'
            f'</li>\n'
        )

    # Close animal details and card
    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"

    return output


# Read JSON data
animals_data = load_data("animals_data.json")


# Generate HTML for all animals
output = ""

for animal_obj in animals_data:
    output += serialize_animal(animal_obj)
# TEMPORARY CHECK
print(output)

# Read HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()


# Replace placeholder with generated animal HTML
new_html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output,
)


# Create final HTML file
with open("animals.html", "w") as file:
    file.write(new_html)