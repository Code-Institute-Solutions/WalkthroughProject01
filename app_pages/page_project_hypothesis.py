import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect malaria-parasitised cells have clear marks/signs, "
        f"typically in the middle of the cell, that can differentiate them from an uninfected cell. \n\n"
        f"* An Image Montage shows that typically a parasitised cell has purplish marks across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
