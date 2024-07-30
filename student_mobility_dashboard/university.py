import streamlit as st
from university_profile import University


def get_university_info(university):
    # Format the details in a list with line breaks
    details = [
        f"**Country:** {university.country}",
        f"**QS Ranking:** {university.qs_ranking}",
        f"**Monthly Expenses:** {university.monthly_expenses} EUR",
        f"**Summer Temperature Average:** {university.summer_temp_ave} °C",
        f"**Winter Temperature Average:** {university.winter_temp_ave} °C",
        f"**Social Activity Level:** {university.social_activity_level}",
        f"**Visa Assistance:** {'Yes' if university.visa_assistance else 'No'}",
        f"**Sustainability Score:** {university.sustainability_score}",
        f"**Gym Amenities:** {university.gym_amenities}",
        f"**Safety Rating:** {university.safety_rating}",
        f"**Language Support:** {university.language_support}"
    ]
    return details


def main():
    st.title("University Information")

    # Get the university from session state
    university = st.session_state.get('selected_university')

    if university:
        st.header(university.name)
        st.subheader("Details")

        # Display each detail on a new line
        details = get_university_info(university)
        for detail in details:
            st.write(detail)

        if st.button('Back to Dashboard'):
            st.session_state.current_page = 'dashboard'
            st.session_state.selected_university = None
            st.experimental_rerun()
    else:
        st.write("No university selected.")


if __name__ == "__main__":
    main()
