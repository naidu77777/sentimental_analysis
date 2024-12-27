# Sentimental Analysis Web Application

This project is a web application designed to perform sentiment analysis on restaurant reviews. It utilizes a Logistic Regression model that has been trained on a dataset of reviews to classify them as either positive or negative. The application is implemented using the Flask web framework, making it easy to set up and use as a lightweight, user-friendly interface for analyzing sentiment.



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Installation

To get started with this project, follow these steps:

#Step 1: **Clone the repository**:
    First, clone the project repository from GitHub using the following command:

    ```bash
    git clone https://github.com/Yash-030/Sentimental_Analysis.git
    cd Sentimental_Analysis
    ```

Step 2: **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

Step 3: **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

Step 4: **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

Step 5: **Download NLTK data**:
    Open a Python shell and run the following commands:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    ```

Step 6: **Run the application**:
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

│ └── start.html


- **app.py**: This is the main application file that sets up and runs the Flask server. It handles user input, calls the sentiment analysis logic, and displays the results on the web interface.
- **sentiment_analysis.py**: This script contains all the core logic for:

Preprocessing the text data.
Training the Logistic Regression model.
Making predictions based on new reviews..
- **Reviews.csv**: This CSV file contains the dataset of restaurant reviews used for training the sentiment analysis model. It includes labeled examples of positive and negative reviews.
- **requirements.txt**: A list of all Python libraries required to run the application. These include:

Flask
NLTK
Scikit-learn
Pandas, etc.
- **templates/index.html**: The HTML template for the web interface.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

