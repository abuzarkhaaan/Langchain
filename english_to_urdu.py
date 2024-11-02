import streamlit as st
from transformers import pipeline

# Initialize the Hugging Face translation pipeline
translator = pipeline("translation_en_to_ur", model="Helsinki-NLP/opus-mt-en-ur")

# Set up the Streamlit interface
st.title("English to Urdu Translator")

# Text input for user to type in their English text
english_text = st.text_area("Enter English text to translate:", "")

# Button to perform translation
if st.button("Translate"):
    if english_text:
        # Run translation
        translation_result = translator(english_text)[0]['translation_text']
        
        # Display translation result
        st.subheader("Translation Result:")
        st.write(translation_result)
    else:
        st.write("Please enter some text for translation.")
