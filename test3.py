from langchain_community.llms.ai21 import AI21
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st

ai21_key = '4hFLnihPfvvFf1TaVXLV2d6IU72l7QIc'

st.set_page_config(page_title="Language Translator", page_icon="🌐")

# Define a list of languages
languages = ["English", "Hindi", "Tamil", "Spanish", "French", "German", "Chinese", "Korean"]

# Sidebar configuration
st.sidebar.title('Language Translator Settings')
source_language = st.sidebar.selectbox("Select source language", languages)
target_language = st.sidebar.selectbox("Select target language", languages)

# Main page title
st.title('Language Translator')

# Input text box
input_text = st.text_input("Enter any sentence")

# Define the prompt template
demo_template = "Translate this sentence from {source_language} to {target_language}: {text}"
prompt = PromptTemplate(
    input_variables=['source_language', 'target_language', 'text'],
    template=demo_template
)

# Initialize the AI21 LLM and output parser
llm = AI21(temperature=0.8, ai21_api_key=ai21_key)
output_parser = StrOutputParser()

# Create a runnable sequence
sequence = prompt | llm | output_parser

# Invoke the sequence and display the translation
if input_text:
    st.write("### Translation:")
    st.write(sequence.invoke({
        'source_language': source_language.lower(),
        'target_language': target_language.lower(),
        'text': input_text
    }))

# Styling
st.markdown("""
    <style>
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #d1e32b; /* Dark blue */
        color: #f39c12; /* Bright yellow */
        font-family: 'Arial', sans-serif;
    }
    
    /* Main page styling */
    .css-18e3th9 {
        background-color: #1c1a1a;
        color: #826279;
        font-family: 'Arial', sans-serif;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        font-size: 16px;
        padding: 10px;
        font-family: 'Arial', sans-serif;
        background-color: #7c86a3; 
        color: #080317; 
    }
    
    /* Button styling */
    .stButton > button {
        font-size: 16px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    
    /* Title styling */
    .css-10trblm {
        font-family: 'Arial', sans-serif;
        color: #f39c12;
    }

    /* Heading styling */
    .css-1v0mbdj {
        font-family: 'Arial', sans-serif;
        color: #f39c12; 
    }
    </style>
""", unsafe_allow_html=True)
