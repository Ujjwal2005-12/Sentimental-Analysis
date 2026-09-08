import streamlit as st
import joblib

model=joblib.load("emotion_model.pkl")
tfidf_vectorizer=joblib.load("tfidf_vectorizer.pkl")
emotion_mapping = joblib.load("emotion_mapping.pkl")
emotion_mapping = {
    value: key for key, value in emotion_mapping.items()
}

st.set_page_config(
    page_title="Emotion AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Emotion AI")
st.subheader("Understand the emotion behind your words")

st.write(
    "Enter a sentence below and our NLP model will analyze "
    "the emotion expressed in the text."
)

st.divider()

st.markdown("### ✍️ Your Message")

text = st.text_area(
    "Enter your text",
    placeholder="Example: I am feeling really happy about my achievement!",
    height=150,
    label_visibility="collapsed"
)

if st.button("✨ Analyze Emotion", use_container_width=True):

    if not text.strip():

        st.warning("Please enter some text first.")
    else:
        text_tfidf=tfidf_vectorizer.transform([text])
        prediction=model.predict(text_tfidf)[0]
        emotion=emotion_mapping[int(prediction)]

        st.divider()

        st.markdown("### 🎯 Detected Emotion")

        st.success(f"### {emotion.upper()}")