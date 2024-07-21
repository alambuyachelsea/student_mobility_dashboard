import streamlit as st
from itertools import batched
from university_profile import University
import csv
from PIL import Image
import base64
from io import BytesIO


def read_file(path):

    universities = []
    header = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Capture the header row
        header = next(reader)

        for row in reader:
            name, qs_ranking, monthly_expenses, summer_temp_ave, winter_temp_ave, social_activity_level, country, visa_assistance, sustainability_score, gym_amenities, safety_rating, language_support = row

            university = University(
                name=name,
                qs_ranking=int(qs_ranking),
                monthly_expenses=int(monthly_expenses),
                summer_temp_ave=float(summer_temp_ave),
                winter_temp_ave=float(winter_temp_ave),
                social_activity_level=int(social_activity_level),
                country=country,
                visa_assistance=bool(int(visa_assistance)),
                sustainability_score=int(sustainability_score),
                gym_amenities=int(gym_amenities),
                safety_rating=int(safety_rating),
                language_support=int(language_support)
            )
            universities.append(university)

    return header, universities


def create_checkboxes(options):
    # Helper function to create multiple checkboxes from a list of options.
    return [st.checkbox(option) for option in options]


def create_slider(label, min_value, max_value, step):
    # Helper function to create a slider.
    return st.slider(
        label, min_value=min_value, max_value=max_value, step=step)


def populate_filters(header):

    sliders = []
    """ Populates the sidebar with expanders, checkboxes,
        and sliders based on the header list. """

    with st.sidebar:
        st.header("What matters most to you")

        for category in header:
            with st.expander(category):
                match category:
                    case "QS Global Ranking":
                        # Example slider for QS Global Ranking
                        ranking_slider = create_slider(
                            "QS Global Ranking",
                            min_value=50, max_value=400, step=1)
                        sliders.append(ranking_slider)

                    case "Monthly Expenses (EUR)":
                        # Example slider for Monthly Expenses
                        expense_slider = create_slider(
                            "Monthly Expenses (EUR)", min_value=450,
                            max_value=1500, step=50)
                        sliders.append(expense_slider)

                    case "Summer Temperature Average":
                        # Example slider for Summer Temperature Average
                        summer_slider = create_slider(
                            "Summer Temperature Average (°C)",
                            min_value=15, max_value=40, step=1)
                        sliders.append(summer_slider)

                    case "Winter Temperature Average":
                        # Example slider for Winter Temperature Average
                        winter_silder = create_slider(
                            "Winter Temperature Average (°C)",
                            min_value=-10, max_value=15, step=1)
                        sliders.append(winter_silder)

                    case "Social Activity Level":
                        # Example slider for Social Activity Level
                        create_slider("Social Activity Level",
                                      min_value=1, max_value=5, step=1)

                    case "Country":
                        # Example checkboxes for countries
                        options = ["Mystara", "Brimstone", "Solari"]
                        create_checkboxes(options)

                    case "Visa Assistance":
                        # Example checkboxes for Visa Assistance
                        options = ["Yes", "No"]
                        create_checkboxes(options)

                    case "Environmental Sustainability Score":
                        # Example slider for Environmental Sustainability Score
                        create_slider("Environmental Sustainability Score",
                                      min_value=1, max_value=5, step=1)

                    case "Gym and Amenities":
                        # Example checkboxes for Gym and Amenities
                        options = ["Gym", "Pool", "Tennis Court"]
                        create_checkboxes(options)

                    case "Safety Rating":
                        # Example slider for Safety Rating
                        create_slider("Safety Rating", min_value=1,
                                      max_value=5, step=1)

                    case "Language Support":
                        # Example checkboxes for Language Support
                        options = ["Faldurian", "Zephorix", "Virellian"]
                        create_checkboxes(options)


grouped = []

# Get the universities from csv
# Read the CSV file
file_path = 'university_data.csv'
header, universities = read_file(file_path)

st.set_page_config(layout="wide")
st.title("Mobility Hub")

populate_filters(header)

# Create a text input for the user to specity country or university name
left, right = st.columns([3, 1])
left.text_input("user input", "Enter a country or university name:",
                label_visibility="collapsed")
right.button("Search", use_container_width=True)


for batch in batched(universities, 3):
    grouped.append(list(batch))


for group in grouped:
    row = st.columns(3)

    for i, col in enumerate(row):
        try:
            school = group[i]
            university_image_path = f'{school.name}.jpg'

            # Load and resize the image
            university_image = Image.open(university_image_path)
            university_image = university_image.resize((700, 300))

            # Convert image to base64
            buffered = BytesIO()
            university_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            # Create a unique ID for the tile to inject CSS
            unique_id = f"tile_{i}_{id(school)}"

            # Debugging: Print the base64 string
            print(f"Base64 string for {school.name}: {img_str[:30]}...")

            # HTML and CSS for the tile
            tile_html = f"""
            <div id="{unique_id}" class="tile">
                <p style="
                color: white;
                text-shadow: 2px 2px 4px #000000;
                font-size: 20px;
                text-align: left;
                ">
                    {school.name},<br>{school.country}
                </p>
            </div>
            <style>
                #{unique_id} {{
                    background-image: url(data:image/jpeg;base64,{img_str});
                    background-size: cover;
                    background-position: center;
                    height: 120px;
                    display: flex;
                    align-items: flex-end;  /* Align items at the bottom */
                    justify-content: flex-start; /* Align items to the left */
                    border-radius: 10px;
                    margin: 10px;
                }}
            </style>
            """

            # Debugging: Print the HTML and CSS
            print(f"HTML and CSS for {school.name}:\n{tile_html}")

            # Inject the HTML and CSS into the Streamlit app
            col.markdown(tile_html, unsafe_allow_html=True)

        except IndexError:
            print(
                f"IndexError: index {i} is out of range for the list.")
