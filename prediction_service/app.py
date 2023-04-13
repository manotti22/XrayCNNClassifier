import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
"""
# Xraydeep Classifier project
"""
model = tf.keras.models.load_model("model.h5")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = Image.open(uploaded_file)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    if argmax_index[1] == 1:
        st.image(image, caption="predicted: Flair")
    elif argmax_index[2] == 2:
        st.image(image, caption="predicted: LesionSeg-Flair")
    elif argmax_index[3] == 3:
        st.image(image, caption="predicted: LesionSeg-T1")
    elif argmax_index[4] == 4:
        st.image(image, caption="predicted: LesionSeg-T2")   
    elif argmax_index[5] == 5:
        st.image(image, caption="predicted: T1")
    elif argmax_index[6] == 6:
        st.image(image, caption="predicted: T2")    
    else:
        st.image(image, caption='predicted: NOTHING')