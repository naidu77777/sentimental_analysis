import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from model.utils import preprocess_text
import os
import nltk

# Ensure necessary NLTK data is available
def download_nltk_data():
    resources = ['stopwords', 'punkt', 'wordnet', 'punkt_tab']
    for res in resources:
        try:
            if res == 'punkt':
                nltk.data.find('tokenizers/punkt')
            elif res == 'punkt_tab':
                nltk.data.find('tokenizers/punkt_tab/english.pickle')
            else:
                nltk.data.find(f'corpora/{res}')
        except LookupError:
            nltk.download(res)

download_nltk_data()

# Define model path
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

def train_model():
    # Load dataset
    df = pd.read_csv("C:/Users/Janar/OneDrive/Desktop/SAnalsis/Reviews.csv")

    # Validate column names
    if 'Review' not in df.columns or 'Liked' not in df.columns:
        print("Available columns:", df.columns)
        raise KeyError("The dataset must contain 'Review' and 'Liked' columns.")

    # Preprocess the reviews
    df['Review'] = df['Review'].apply(preprocess_text)

    # Prepare features and labels
    X = df['Review']
    y = df['Liked']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize using TF-IDF
    tfidf = TfidfVectorizer()
    X_train_tfidf = tfidf.fit_transform(X_train)

    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)

    # Save model and vectorizer
    with open(model_path, 'wb') as f:
        pickle.dump((tfidf, model), f)

    print("✅ Model training completed and saved to model.pkl")

if __name__ == "__main__":
    train_model()
