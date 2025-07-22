import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Uncomment this if you're running it the first time
# nltk.download('punkt')
# nltk.download('stopwords')

ps = PorterStemmer()

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# Streamlit app title
st.title("📩 Email/SMS Spam Classifier")

# Input text area with increased height
input_sms = st.text_area("Enter the message:", height=300)

# Predict button
if st.button('Predict'):

    # Display the original input message
    st.subheader("Your input message:")
    st.write(input_sms)

    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    # 4. Display the result
    st.subheader("Prediction:")
    if result == 1:
        st.header("It is a 🚨 Spam")
    else:
        st.header(" ✅ It is not a  Spam message")
