import streamlit as st


def page_page_malaria_detector_body():
    st.write("### page_malaria_detector")
    st.info(
        f"* 2 - The client is interested to tell whether or not a given cell is parasitized "
        f"with malaria or not."
        )


    from PIL import Image
    import numpy as np
    img_file_buffer = st.file_uploader('Upload the blood smear sample', type='png')
    st.write("---")
    if img_file_buffer is not None:
        img = np.array((Image.open(img_file_buffer)))
        st.image(img, caption=f"{img.shape}")
        
        
        import cv2
        img_resized = cv2.resize(img,(133,132)) 
        my_image = np.expand_dims(img_resized, axis=0)

        from tensorflow.keras.models import load_model
        model = load_model('outputs/model/my_model.h5')
        pred_proba = model.predict(my_image)[0,0]
        st.write(pred_proba)