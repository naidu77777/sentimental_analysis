import pickle
from model.utils import preprocess_text
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

def predict_sentiment(review):
    with open(model_path, 'rb') as f:
        tfidf, model = pickle.load(f)

    cleaned = preprocess_text(review)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)
    return prediction[0]