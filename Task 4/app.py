import streamlit as st
import pickle
import re

def transform_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Load the saved model and vectorizer
loaded_model = pickle.load(open('spam_model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


def predict_spam(text):
    transformed_text = transform_text(text)
    vectorized_text = loaded_vectorizer.transform([transformed_text])
    prediction = loaded_model.predict(vectorized_text)[0]
    return prediction


tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('spam_model.pkl','rb'))

st.title("Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = loaded_vectorizer.transform([transformed_sms])
    # 3. predict
    result = loaded_model.predict(vector_input)[0]
    # 4. Display
    if result == 0:
        st.header("Spam")
    else:
        st.header("Not Spam")