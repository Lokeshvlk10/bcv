import streamlit as st
import cv2
import numpy as np

def apply_transformation(image, transformation_method):
    if transformation_method == 'Grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif transformation_method == 'Blur':
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif transformation_method == 'Canny Edge Detection':
        return cv2.Canny(image, 100, 200)
    elif transformation_method == 'Rotate 90 Degrees':
        return np.rot90(image)
    elif transformation_method == 'Invert Colors':
        return cv2.bitwise_not(image)
    elif transformation_method == 'Sepia':
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        return cv2.transform(image, sepia_filter)
    else:
        return image

def main():
    st.title("Image Transformation App")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        transformation_method = st.selectbox("Choose a transformation method:", ['Grayscale', 'Blur', 'Canny Edge Detection', 'Rotate 90 Degrees', 'Invert Colors', 'Sepia'])

        if st.button("Apply Transformation"):
            transformed_image = apply_transformation(image, transformation_method)
            st.image(transformed_image, caption="Transformed Image", use_column_width=True)

if __name__ == "__main__":
    main()
