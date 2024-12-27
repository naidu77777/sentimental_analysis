# Sentimental Analysis Web Application

This project is a web application designed to perform sentiment analysis on restaurant reviews. It utilizes a Logistic Regression model that has been trained on a dataset of reviews to classify them as either positive or negative. The application is implemented using the Flask web framework, making it easy to set up and use as a lightweight, user-friendly interface for analyzing sentiment.



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Installation

To get started with this project, follow these steps:

step 1: **Clone the repository**:
    First, clone the project repository from GitHub using the following command:

    ```bash
    git clone https://github.com/Yash-030/Sentimental_Analysis.git
    cd Sentimental_Analysis
    ```

3. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Download NLTK data**:
    Open a Python shell and run the following commands:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

7. **Run the application**:
    ```bash
    python app.py
    ```

## Usage

After starting the application, open your web browser and go to `http://127.0.0.1:5000`. You will see a simple web interface where you can enter a restaurant review. Submit the review to see whether it is classified as positive or negative.

## Project Structure

sentimental_Analysis_webapp/

├── app.py

├── sentiment_analysis.py

├── Reviews.csv

├── requirements.txt

├── templates/

│ └── index.html


- **app.py**: The main Flask application file.
- **sentiment_analysis.py**: Contains the preprocessing, training, and prediction logic.
- **Reviews.csv**: The dataset used for training the sentiment analysis model.
- **requirements.txt**: Lists all the dependencies required for the project.
- **templates/index.html**: The HTML template for the web interface.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

