
import pandas as pd
import streamlit as st
import numpy as np
from joblib import load

def expression_check(prediction_input):

    if prediction_input == -1:
        print("👎🏻 Negative Sentiment.")
    elif prediction_input == 1:
        print("👍🏻 Positive Sentiment.")
    else:
        print("Invalid Statement.")

# function to take the input statement and perform the same transformations we did earlier
def sentiment_predictor(input):
    input = text_transformation(input)

    lr1 = load("lr1.pkl")
    tfidf1 = load("tfidf.pkl")

    transformed_input=tfidf1.transform(input)
    prediction = lr1.predict(transformed_input)
    expression_check(prediction)

# Sayfa Ayarları
st.set_page_config(
    page_title="NlP - Sentiment Analysis",
    page_icon="",
    layout="centered",
    menu_items={
        "Get help": "mailto:nygulzehra@gmail.com",
        "About": "For More Information\n" + "https://github.com/nygulzehra"
    }
)

st.title("**black[Review Sentiment Analysis Project]**")
st.image("pos-neg.png")
st.markdown("Let's try ! ")

st.subheader("*:blue[Let's try sentiment analysis using machine learning!]*")
text = st.text_input("Write here" )

    # Sonuç Ekranı
if st.button("Submit"):

    st.info("*result*")
    sentiment_predictor(text)
