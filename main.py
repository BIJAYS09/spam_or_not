import streamlit as st
import pickle
import sklearn.metrics._scorer

def _passthrough_scorer():
    pass

sklearn.metrics._scorer._passthrough_scorer = _passthrough_scorer

#Load the model
with open('data_spam_classifier.pkl', 'rb') as file:
    loaded_pipe = pickle.load(file)    

# Function to predict user input
def predict_spam(message):
    prediction = loaded_pipe.predict([message])
    return 'Spam' if prediction[0] == 1 else 'Not Spam'

# Example usage with user input
user_input = "URGENT! You have won a 1 week FREE membership in our å£100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18"
print(f"Message: {user_input}")
print(f"Prediction: {predict_spam(user_input)}")

st.title("Is your Email/SMS a Spam or not? Find it here?")

input_sms = st.text_area("Enter the message")

if st.button("Predict"):
    result = predict_spam(input_sms)
    #Display
    st.header(result)