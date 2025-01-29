import streamlit as st
import joblib

# Load the saved TF-IDF vectorizer and model
tfidf = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('genre_classification_model.pkl')

# Streamlit UI
st.title("Movie Genre Classification")
st.write("Enter a movie description, and the model will predict its genre.")

# Text input for user
description = st.text_area("Movie Description", "Type here...")

if st.button("Predict Genre"):
    if description.strip():
        # Transform input using the loaded TF-IDF vectorizer
        input_vector = tfidf.transform([description])
        
        # Predict the genre
        predicted_genre = model.predict(input_vector)[0]
        
        # Display the prediction
        st.success(f"Predicted Genre: {predicted_genre}")
    else:
        st.warning("Please enter a movie description before predicting.")