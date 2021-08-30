import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv, download_file
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_page_malaria_detector_body():
    st.info(
        f"* The client is interested to tell whether or not a given cell is parasitized "
        f"with malaria or not."
        )

    st.write(
        f"* You can download a set of Parasitized and Uninfected Cells for live prediction. "
        f"These cells were not used to train the model."
        )

    st.markdown(
        download_file(
                    bin_file='inputs/live_data/cell_images.zip',
                    file_label='cell_images.zip'),
        unsafe_allow_html=True
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload blood smear samples. You may select more than one.',
                                        type='png',accept_multiple_files=True)
   
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img = np.array((Image.open(image)))
            st.info(f"Blood Smear Sample: **{image.name}**")
            
            st.image(img, caption=f"Image Size: {img.shape[1]}px width x {img.shape[0]}px height")
            resized_img = resize_input_image(img)

            pred_proba, pred_class = load_model_and_predict(resized_img)
            plot_predictions_probabilities(pred_proba, pred_class)
            df_report = df_report.append({"Name":image.name, 'Result': pred_class }, ignore_index=True)
        

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)


