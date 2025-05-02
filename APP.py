from flask import Flask, request, render_template
from model.predict import predict_sentiment  # Assuming this handles sentiment prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('INDEX.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        if not review.strip():  # Check for empty input
            return render_template('INDEX.html', prediction="Please enter a valid review.", review=review)
        
        sentiment = predict_sentiment(review)
        
        # Check the type of sentiment prediction, if it's numeric, you may want to map it
        sentiment_label = ""
        if sentiment == 1:
            sentiment_label = "Positive"
        elif sentiment == 0:
            sentiment_label = "Negative"
        
        else:
            sentiment_label = "Unknown"
        
        return render_template('INDEX.html', prediction=sentiment_label, review=review)

if __name__ == '__main__':
    app.run(debug=True)
