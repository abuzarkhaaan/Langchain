# Mini Projects: Sentiment Analysis and English-to-Urdu Translator

This repository contains two mini projects:

1. **Sentiment Analysis**: A web app that analyzes the sentiment (Positive, Negative, Neutral) of input text.
2. **English-to-Urdu Translator**: A web app that translates English text to Urdu.

Both projects are deployed on Streamlit and use the Hugging Face API for NLP tasks, with LangChain facilitating the orchestration of models and integrations.

## Project 1: Sentiment Analysis

### Overview
The **Sentiment Analysis** project allows users to input text and receive a sentiment label—**Positive**, **Negative**, or **Neutral**—based on the content. This is useful for understanding the general tone of statements or reviews.

### Technologies Used
- **Streamlit**: Used to create an interactive web application.
- **Hugging Face Transformers**: `pipeline` for sentiment analysis, using models like `distilbert-base-uncased-finetuned-sst-2-english`.
- **LangChain**: Set up for potential expansions or orchestrating more complex model interactions.

### Features
- Accepts user input for analysis.
- Detects sentiment and provides a confidence score.
- Classifies sentiment as **Positive**, **Negative**, or **Neutral** (based on a confidence threshold).
