# -*- coding: utf-8 -*-
import streamlit as st
import os

st.set_page_config(page_title="Fish Classification", layout="centered")

st.title("🐟 Fish Species Classification")
st.write("Upload a fish image to predict its species.")

MODEL_PATH = "tinycnn_fish.pt"

if not os.path.exists(MODEL_PATH):
    st.warning("Model file not found yet.")
    st.info("Expected file name: tinycnn_fish.pt")
else:
    st.success("Model file found. Ready for prediction.")

uploaded = st.file_uploader(
    "Upload a fish image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    st.image(uploaded, caption="Uploaded Image", use_column_width=True)
    st.info("Prediction logic will activate once model is loaded.")
