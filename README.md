# English to Urdu Translation and Sentiment Analysis via LangChain

## Project 1: English to Urdu Translation

### Overview
This project aims to translate text from English to Urdu using the capabilities of LangChain, a framework for creating applications using large language models. By leveraging LangChain, this project provides a seamless interface for high-quality translations, preserving meaning and context to cater to Urdu speakers.

### Features
- **High-Quality Translation**: Accurately translates English text to Urdu, maintaining the meaning and cultural context.
- **User-Friendly Interface**: Uses a simple UI to input English text and get Urdu translations.
- **Scalable Solution**: Easily adaptable for different domains like education, social media, or official documentation.

### Dataset
The dataset used includes publicly available translation pairs for English to Urdu, which include:
- **Conversational Sentences**: Common phrases used in everyday conversations.
- **Literary Text**: A mix of sentences from articles and literature to capture nuanced language.

### Requirements
To run this translation system using LangChain, you will need:

- Python 3.8+
- **LangChain** for managing language model pipelines
- **Hugging Face Transformers** for model integration
- **Streamlit** for building a simple front-end interface

You can install the required packages using:
```sh
pip install langchain transformers streamlit
```

### Running the Translation
To run the translation system, follow these steps:

1. **Start the Streamlit Interface**:
   ```sh
   streamlit run translate_app.py
   ```
   - This will open a UI where you can input text in English and get the Urdu translation.

2. **Translation Process**:
   - The input English text is processed using a pre-trained translation model from Hugging Face, managed via LangChain for efficient query handling.

## Project 2: Sentiment Analysis via LangChain

### Overview
The sentiment analysis project aims to determine the sentiment (positive, negative, or neutral) of a given text using LangChain. By leveraging advanced language models, the project ensures accurate and nuanced sentiment evaluation, even for complex sentences and mixed emotions.

### Features
- **Sentiment Categorization**: Classifies text as positive, negative, or neutral.
- **Multi-Domain Support**: Works well with texts from social media, product reviews, and general articles.
- **Real-Time Analysis**: Provides sentiment analysis in real-time for fast feedback.

### Dataset
The dataset for training the sentiment analysis model consists of:
- **Twitter Data**: Tweets labeled as positive, negative, or neutral.
- **Product Reviews**: Reviews from e-commerce platforms that provide a varied range of sentiments.

### Requirements
To run the sentiment analysis system using LangChain, you will need:

- Python 3.8+
- **LangChain** for managing language model workflows
- **Transformers** from Hugging Face for the sentiment analysis model
- **Gradio** for building a user-friendly web interface

You can install the required packages using:
```sh
pip install langchain transformers gradio
```

### Running the Sentiment Analysis
To run the sentiment analysis system, follow these steps:

1. **Start the Gradio Interface**:
   ```sh
   python sentiment_analysis_app.py
   ```
   - This will open a Gradio interface where users can input text and receive a sentiment analysis result.

2. **Sentiment Analysis Process**:
   - The input text is analyzed using a pre-trained model from Hugging Face, managed through LangChain to streamline the process and improve efficiency.

## Deployment
Both projects can be deployed in multiple ways for broader usage:
- **Web Application**: Deployed using either Streamlit (for translation) or Gradio (for sentiment analysis) to create a user-friendly web experience.
- **Cloud Services**: Deploy on cloud platforms such as AWS or Google Cloud to make the services accessible to a wider audience.
- **API Integration**: Both services can be made available via APIs, allowing other applications to integrate translation and sentiment analysis features.

## Future Work
- Expand the translation model to include more languages, such as French and Arabic, using LangChain for seamless integration.
- Improve sentiment analysis by adding more categories, such as "mixed feelings" or "sarcasm," to handle complex emotions.
- Add user authentication to the web applications for a personalized experience.

## Acknowledgments
- **LangChain** for providing an easy way to create LLM-based workflows.
- **Hugging Face** for the pre-trained models used for translation and sentiment analysis.
- **Streamlit and Gradio** for simple and efficient user interface development.

## License
These projects are licensed under the MIT License. Please see the LICENSE file for more details.
