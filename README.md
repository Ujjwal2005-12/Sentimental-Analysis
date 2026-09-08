# 🧠 Emotion AI — NLP Emotion Classification

> An NLP-based machine learning application that predicts the emotion expressed in a piece of text using **TF-IDF Vectorization** and **Logistic Regression**.

---

## ✨ Overview

Emotion AI is a Natural Language Processing (NLP) project designed to classify text into one of six emotions.

The project explores how different text representations and machine learning algorithms perform on an emotion classification task.

The final model uses:

**Text → Preprocessing → TF-IDF → Logistic Regression → Emotion**

The trained model is integrated into a **Streamlit web application**, allowing users to enter text and receive an emotion prediction instantly.

---

## 🎯 Problem Statement

Human language contains emotional information that can be useful for applications such as:

- 💬 Conversational AI
- 📱 Social media analysis
- 🧠 Sentiment and emotion understanding
- 🤖 Customer feedback analysis
- 📊 Text analytics

The objective of this project is to build a machine learning system capable of identifying the emotion expressed in a given text.

---

## 📊 Dataset

The project uses a text-based emotion classification dataset containing:

- **16,000 text samples**
- **2 columns**
  - `text` — Input sentence
  - `emotion` — Target emotion
- **6 emotion classes**

### Emotion Classes

| Emotion | Label |
|---|---:|
| 😢 Sadness | 0 |
| 😡 Anger | 1 |
| ❤️ Love | 2 |
| 😮 Surprise | 3 |
| 😨 Fear | 4 |
| 😊 Joy | 5 |

---

## 🔄 NLP Pipeline

The project follows the following pipeline:

```text
                Raw Text
                   │
                   ▼
          Text Preprocessing
                   │
          ┌────────┴────────┐
          │                 │
     Lowercasing       Remove Punctuation
          │                 │
          └────────┬────────┘
                   ▼
           Remove Numbers
                   │
                   ▼
            Remove Emojis
                   │
                   ▼
          Remove Stopwords
                   │
                   ▼
             TF-IDF
                   │
                   ▼
       Logistic Regression
                   │
                   ▼
        Predicted Emotion
