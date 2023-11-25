# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import streamlit as st
from streamlit.logger import get_logger

# Load the pre-trained model
#model = tf.keras.models.load_model('path/to/your/pretrained_model.h5')

# Function to preprocess the image before feeding it to the model
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.asarray(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction

# Streamlit app
def main():
    st.title("Breast Cancer Detection App")
    st.write(
        "This app uses a deep learning model to predict whether an uploaded image contains signs of breast cancer."
    )

    st.sidebar.success("Select a demo above.")


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Make predictions when the 'Predict' button is clicked
        if st.button("Predict"):
            prediction = predict(image)
            if prediction[0][0] > 0.5:
                st.success("The model predicts that this image contains signs of breast cancer.")
            else:
                st.success("The model predicts that this image does not contain signs of breast cancer.")
LOGGER = get_logger(__name__)



  
  
if __name__ == "__main__":
    main()



