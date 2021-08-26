import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_cells_visualizer import page_cells_visualizer_body
from app_pages.page_malaria_detector import page_page_malaria_detector_body

# Create an instance of the app 
app = MultiPage() 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cells Visualizer", page_cells_visualizer_body)
app.add_page("Malaria Detection", page_page_malaria_detector_body)


# Run the  app
app.run(app_name= "Malaria Detector")