import streamlit as st
from university_profile import University
from streamlit.errors import DuplicateWidgetID
import csv
from PIL import Image
import base64
from io import BytesIO

# Global variables
universities = []
st.session_state.filtered_universities = []


def read_file(file_path):
    global universities
    universities = []
    header = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
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

    st.session_state.filtered_universities = universities

    return header


def create_slider(label, min_value, max_value, step):
    """Creates a slider with the given parameters and initializes its value in session state if not set."""
    slider_key = f"slider_{label.replace(
        ' ', '_').replace('(', '').replace(')', '')}"
    if slider_key not in st.session_state:
        st.session_state[slider_key] = min_value
    return st.slider(label, min_value=min_value, max_value=max_value, step=step, key=slider_key)


def create_checkboxes(options, category):
    """Creates a set of checkboxes for the given options and initializes their states in session state if not set.
    Skips creation if the key is not unique."""
    checkbox_keys = [f"{category}_{
        option.replace(' ', '_')}" for option in options]
    values = []

    # Create a set to track already used keys
    used_keys = set(st.session_state.keys())

    for key, option in zip(checkbox_keys, options):
        if key not in used_keys:
            try:
                st.session_state[key] = False
                # Try creating the checkbox and catch DuplicateWidgetID exception
                values.append(st.checkbox(option, key=key))
            except DuplicateWidgetID:
                # Handle the exception by skipping the checkbox creation
                print(f"Duplicate widget ID encountered for key: {
                      key}. Skipping creation.")
                values.append(None)  # Indicate that this checkbox was skipped
        else:
            values.append(None)  # Indicate that this checkbox was skipped

    return values


def filter_universities(universities):

    selected = []

    for school in universities:
        if school.name == "Linneaus University":
            selected.append(school)

    return selected


def populate_filters(header, container):
    """Populates the sidebar with expanders, checkboxes, and sliders based on the header list."""
    with st.sidebar:
        st.header("What matters most to you")

        for category in header:
            with st.expander(category):
                try:

                    match category:
                        case "QS Global Ranking":
                            create_slider("QS Global Ranking",
                                          min_value=50, max_value=400, step=1)

                        case "Monthly Expenses (EUR)":
                            create_slider("Monthly Expenses (EUR)",
                                          min_value=450, max_value=1500, step=50)

                        case "Summer Temperature Average":
                            create_slider("Summer Temperature Average (°C)",
                                          min_value=15, max_value=40, step=1)

                        case "Winter Temperature Average":
                            create_slider("Winter Temperature Average (°C)",
                                          min_value=-10, max_value=15, step=1)

                        case "Social Activity Level":
                            create_slider("Social Activity Level",
                                          min_value=1, max_value=5, step=1)

                        case "Country":
                            create_checkboxes(
                                ["Sweden", "Spain", "France", "Germany"], "Country")

                        case "Visa Assistance":
                            create_checkboxes(["Yes", "No"], "Visa Assistance")

                        case "Environmental Sustainability Score":
                            create_slider(
                                "Environmental Sustainability Score", min_value=1, max_value=5, step=1)

                        case "Gym and Amenities":
                            create_checkboxes(
                                ["Gym", "Pool", "Tennis Court"], "Gym and Amenities")

                        case "Safety Rating":
                            create_slider("Safety Rating",
                                          min_value=1, max_value=5, step=1)

                        case "Language Support":
                            create_checkboxes(
                                ["Faldurian", "Zephorix", "Virellian"], "Language Support")

                except DuplicateWidgetID:
                    # Handle the exception by skipping the checkbox creation
                    print("Duplicate widget ID encountered.")

        # Add the "Apply Filters" button
        if st.button("Apply Filters"):
            selected = []

            for school in universities:
                if school.name == "Linneaus University":
                    selected.append(school)

            st.session_state.filtered_universities = selected
            print(st.session_state.filtered_universities)


def display_schools(universities, container):
    grouped = [universities[i:i + 3] for i in range(0, len(universities), 3)]

    for group in grouped:
        row1 = container.columns(3)
        row2 = container.columns(3)

        for i, col in enumerate(row1):
            if i < len(group):
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
                            align-items: flex-end;
                            justify-content: flex-start;
                            border-radius: 10px;
                            margin: 10px;
                        }}
                    </style>
                    """

                    # Inject the HTML and CSS into the Streamlit app
                    col.markdown(tile_html, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error loading image for {school.name}: {e}")

        for i, col in enumerate(row2):
            if i < len(group):
                school = group[i]
                with col:
                    if st.button("View Details", key=school.name):
                        st.session_state.selected_university = school
                        st.session_state.current_page = 'linneaus_university'
                        st.experimental_rerun()


def main():
    # Read university data
    file_path = 'university_data.csv'
    header = read_file(file_path)

    container = st.container()
    st.title("Student Mobility Dashboard")
    populate_filters(header, container)

    left, right = st.columns([3, 1])
    search_input = left.text_input(
        "Enter a country or university name:", "", label_visibility="collapsed")
    search_button = right.button("Search", use_container_width=True)

    # Create a lower case version of the search input for case-insensitive matching
    search_input_lower = search_input.lower()

    container = st.container()

    st.session_state.filtered_universities = [
        u for u in st.session_state.filtered_universities
        if search_input_lower in u.name.lower() or search_input_lower in u.country.lower()
    ]

    #  print("passed")
    display_schools(st.session_state.filtered_universities, container)


if __name__ == "__main__":
    main()
