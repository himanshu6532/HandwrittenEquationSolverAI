import streamlit as st
import cv2
import pytesseract
import numpy as np
import re

from PIL import Image
from sympy import symbols, Eq, solve

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

x = symbols('x')

st.title("Handwritten Equation Solver AI")

uploaded_file = st.file_uploader("Upload Equation Image")

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image)

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(thresh)

    st.write("Detected Equation:", text)

    equation = text.strip()

    equation = re.sub(r'(\d)(x)', r'\1*\2', equation)

    try:

        left, right = equation.split('=')

        expr = Eq(eval(left), eval(right))

        solution = solve(expr)

        st.success(f"Solution: {solution}")

    except:
        st.error("Could not solve equation")
        