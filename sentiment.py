import streamlit as st
from transformers import pipeline


sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


st.title("Sentiment Analysis Web App")


user_input = st.text_area("Enter text to analyze sentiment:", "")


CONFIDENCE_THRESHOLD = 0.7  


if st.button("Analyze Sentiment"):
    if user_input:
    
        result = sentiment_analyzer(user_input)[0]
        
      
        if result['score'] < CONFIDENCE_THRESHOLD:
            label = "NEUTRAL"
        else:
            label = result['label']  

      
        st.subheader("Sentiment Analysis Result:")
        st.write(f"Label: {label}")
        st.write(f"Confidence Score: {result['score']:.2f}")
    else:
        st.write("Please enter some text for sentiment analysis.")
