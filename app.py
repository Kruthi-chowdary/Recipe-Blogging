import os
import streamlit as st
import google.generativeai as genai

# Set your Gemini AI API key
GEMINI_API_KEY = "AIzaSyDcdn-IEiexJyCqXKkofMPuHUkGXVakgUo"
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate a recipe using Gemini AI
def generate_recipe(topic, word_count):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Write a {word_count}-word recipe blog about {topic}. Include ingredients, steps, and tips.")
        return response.text
    except Exception as e:
        return f"Error generating recipe: {str(e)}"

# Function to generate a joke using Gemini AI
def generate_joke():
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content("Tell me a funny programmer joke.")
        return response.text
    except Exception as e:
        return f"Error generating joke: {str(e)}"

# Streamlit UI
st.title("Flavour Fusion: AI-Driven Recipe Blogging 🍽️")
st.write("Generate unique recipe blogs using Google Gemini AI!")

# User input for recipe topic & word count
topic = st.text_input("Enter Recipe Topic (e.g., Vegan Chocolate Cake):")
word_count = st.number_input("Enter Word Count:", min_value=100, max_value=2000, step=100)

if st.button("Generate Recipe"):
    with st.spinner("Generating recipe... Here's a joke while you wait!"):
        joke = generate_joke()
        st.success("Here's a programmer joke:")
        st.write(joke)

        recipe = generate_recipe(topic, word_count)
        st.subheader("Generated Recipe:")
        st.write(recipe)

