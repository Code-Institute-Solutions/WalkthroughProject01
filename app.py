import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.feedback_generate import feedback_generate

app = MultiPage(app_name="Driver Feedback")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Feedback Generator", feedback_generate)

app.run()  # Run the app
