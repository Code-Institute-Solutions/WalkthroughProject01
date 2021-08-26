import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n"
        f"* Malaria is a parasitic infection transmitted by the bite of infected female "
        f"Anopheles mosquitoes.\n"
        f"* According to [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria), "
        f"in 2019, there were an estimated 229 million cases of malaria worldwide and an "
        f"estimated number of malaria deaths of 409 thousand. "
        f"Children <5 years are the most vulnerable group, accounting for 67% (274 thousand) "
        f"of all malaria deaths worldwide in 2019.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains +27 thousand images taken from "
        f"blood smear workflow (when a drop of blood it taken on a glass slide) of cells that "
        f"are parasitized or uninfected with malaria.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/FernandoRocha88/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested to have a study to visually differentiate "
        f"an parasitized and uninfected cell.\n"
        f"* 2 - The client is interested to tell whether or not a given cell is parasitized "
        f"with malaria or not."
        )

    # st.write("add a image that represents the project")
    # project_snapshot = plt.imread("pictures/requirements.png")
    # st.image(project_snapshot, caption='Representations for Business Requirements 1 and 2, respectively.')