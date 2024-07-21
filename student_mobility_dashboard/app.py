import streamlit as st
import dashboard
import lunar_harbour_college

# Set the page configuration here
st.set_page_config(layout="wide")

# Initialize session state for page tracking and selected university
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

if 'selected_university' not in st.session_state:
    st.session_state.selected_university = None

# Page routing based on session state
if st.session_state.current_page == 'lunar_harbour_college':
    lunar_harbour_college.main()
else:
    dashboard.main()
