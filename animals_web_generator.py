import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")
# PART 2: CREATE STRING WITH ANIMAL INFORMATION
output = ""


for animal in animals_data:
    # Start one animal card
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f"Name: {animal['name']}<br/>\n"

    if "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and animal["locations"]:
        output += f"Location: {animal['locations'][0]}<br/>\n"

    if "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}<br/>\n"

    # End one animal card
    output += "</li>\n"

print(output)

# Read the existing HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()


# Replace the placeholder with our animal information
new_html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output
)


# Create a new HTML file containing the result
with open("animals.html", "w") as file:
    file.write(new_html)