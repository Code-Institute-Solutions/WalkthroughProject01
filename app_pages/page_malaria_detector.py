import streamlit as st
from PIL import Image
import numpy as np


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
        DownloadReport(
                    bin_file='inputs/live_data/cell_images.zip',
                    file_label='cell_images.zip'),
        unsafe_allow_html=True
        )

    st.write("---")


    img_file_buffer = st.file_uploader('Upload a blood smear sample', type='png')
    if img_file_buffer is not None:

        img = np.array((Image.open(img_file_buffer)))
        st.write("* Blood Smear Sample")
        st.image(img, caption=f"Image Size: Width {img.shape[1]}px x Height {img.shape[0]}px")
        my_image = resize_input_image(img)

        pred_proba, pred_class = load_model_and_predict(my_image)
        plot_predictions_probabilities(pred_proba, pred_class)

import os
import base64
def DownloadReport(bin_file, file_label='File'):

    with open(bin_file, 'rb') as f: data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = (
        f'<a href="data:application/octet-stream;base64,{bin_str}" '
        f'download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    )
    return href


import pandas as pd
import plotly.express as px
def plot_predictions_probabilities(pred_proba, pred_class):

    prob_per_class= pd.DataFrame(
            data=[0,0],
            index={'Parasitized': 0, 'Uninfected': 1}.keys(),
            columns=['Probability']
        )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    
    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y=[0,1],
            width=600, height=400,template='seaborn')
    st.plotly_chart(fig)





import cv2      
def resize_input_image(img):        
    # img_resized = cv2.resize(img,(132,133)) 
    img_resized = cv2.resize(img,(130,130)) 
    my_image = np.expand_dims(img_resized, axis=0)
    return my_image

from tensorflow.keras.models import load_model
def load_model_and_predict(my_image):
    # model = load_model('outputs/model/my_model.h5')
    model = load_model('outputs/model/malaria_detector.h5')
    pred_proba = model.predict(my_image)[0,0]

    target_map = {v: k for k, v in {'Parasitized': 0, 'Uninfected': 1}.items()}
    pred_class =  target_map[pred_proba > 0.5]  
    if pred_class == target_map[0]: pred_proba = 1 - pred_proba

    # st.write(pred_class,pred_proba)
    st.write(
        f"* The predictive analysis indicates the sample cell is "
        f"**{pred_class.lower()}** with malaria.")
    
    return pred_proba, pred_class
