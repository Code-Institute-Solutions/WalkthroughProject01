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
        st.image(img, caption=f"{img.shape}")
        
        
        import cv2
        img_resized = cv2.resize(img,(132,133)) 
        my_image = np.expand_dims(img_resized, axis=0)

        from tensorflow.keras.models import load_model
        model = load_model('outputs/model/my_model.h5')
        pred_proba = model.predict(my_image)[0,0]


        target_map = {'Parasitized':1, 'Uninfected':0} # {v: k for k, v in {'Parasitized':1, 'Uninfected':0}}
        pred_class =  target_map[pred_proba > 0.5]  

        # if pred_class == target_map[0]: pred_proba = 1 - pred_proba
        # st.write(target_map,pred_class)


        # prob_per_class= pd.DataFrame(data=[0,0],index=train_image_gen.class_indices.keys(), columns=['Probability'])

        # prob_per_class.loc[pred_class] = pred_proba

        # for x in prob_per_class.index.to_list():
        #     if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba

        # prob_per_class = prob_per_class.round(3)
        # print(prob_per_class)
        # import plotly.express as px
        # fig = px.bar(prob_per_class, x = prob_per_class.index, y = prob_per_class['Probability'],range_y=[0,1],
        #             labels=dict(x="Diagnosis"), width=400, height=500)
        # st.plotly_chart(fig)