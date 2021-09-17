import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect malaria parasitized cell have clear marks/signs, "
        f"typically in the middle of the cell, that can differentiate, from a un-infected cell. \n\n"
        f"* An Image Montage, shows that typically a parasitized cell has purplish marks across. "
        f"Average Image, Variability Image and Difference between Averages studies didn't reveal "
        f"any clear pattern to differentiate one to another."

    )
