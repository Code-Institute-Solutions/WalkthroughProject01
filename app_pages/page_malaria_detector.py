import streamlit as st


def page_page_malaria_detector_body():
    st.write("### page_malaria_detector")
    st.info(
        f"* The client is interested to tell whether or not a given cell is parasitized "
        f"with malaria or not."
        )


    from PIL import Image
    import numpy as np
    img_file_buffer = st.file_uploader('Upload the blood smear sample', type='png')
    st.write("---")
    if img_file_buffer is not None:
        img = np.array((Image.open(img_file_buffer)))
        st.write("* Blood Smear Sample")
        st.image(img, caption=f"{img.shape}")
        
        
        import cv2
        img_resized = cv2.resize(img,(132,133)) 
        my_image = np.expand_dims(img_resized, axis=0)

        from tensorflow.keras.models import load_model
        model = load_model('outputs/model/my_model.h5')
        pred_proba = model.predict(my_image)[0,0]


        target_map = {v: k for k, v in {'Parasitized': 0, 'Uninfected': 1}.items()}
        
        pred_class =  target_map[pred_proba > 0.5]  
        st.write(f"* The predictive analysis indicates the cell is {pred_class.lower()} with Malaria.")

        if pred_class == target_map[0]: pred_proba = 1 - pred_proba

        import pandas as pd
        prob_per_class= pd.DataFrame(data=[0,0],index={'Parasitized': 0, 'Uninfected': 1}.keys(), columns=['Probability'])

        prob_per_class.loc[pred_class] = pred_proba

        import plotly.express as px
        for x in prob_per_class.index.to_list():
            if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba

        prob_per_class = prob_per_class.round(3)
        prob_per_class['Diagnostic'] = prob_per_class.index
        import plotly.express as px
        fig = px.bar(
                prob_per_class,
                x = 'Diagnostic',
                y = prob_per_class['Probability'],
                range_y=[0,1],
                width=600, height=400,template='presentation')

        st.plotly_chart(fig)