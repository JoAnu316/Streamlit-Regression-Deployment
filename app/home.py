import streamlit as st

def home_page():
    st.info("Welcome to my web page. Let us help you predict the price of your desired house ")

    st.image("house image.jpg", caption = "House Image")

    st.markdown("""
    <h3 style = "colour:blue;">
    Predicting house prices can be a...
    </h3>
    """)

    st.markdown("""
        ### How it works:
        1. nout the feature 
    """)

    st.markdown("""
        ### About this project:
    """)

    st.info("""
        This project uses a dataset that contains house pricing data from califonia
    """)