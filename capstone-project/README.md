# Beer Recommender System

This is a Flask-based application that uses a machine learning model to recommend beers based on user input. The user interacts with the app via an HTML-based chatbot, which collects preferences and displays recommendations.

## Project Structure

recommender-app/
  - rec_app.py                # The main Flask app script
  - beer_recommender_model.pkl # Pre-trained machine learning model
  - requirements.txt          # Required dependencies
  - chatbot.html              # HTML interface for user interaction (chatbot)

## Prerequisites
Before running the application, ensure that you have the following installed on your local machine:

 - Python 3.7 or above
 - pip (Python package installer)
 - Flask and other required libraries (specified in requirements.txt)

## Getting Started
1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/rohithk9/mle-springboard.git
cd recommender-app

2. Set Up a Virtual Environment (optional)
Set up a virtual environment to keep dependencies isolated:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install the required Python packages using pip and the requirements.txt file:

pip install -r requirements.txt

4. Run the Flask App
Run the Flask app locally by executing the following command:

python3 rec_app.py

5. Open the Chatbot Interface
To interact with the chatbot, open the chatbot.html file in your browser. This file sends input to the Flask app and displays beer recommendations based on user preferences.

6. Stop the Flask App
To stop the Flask server, press Ctrl+C in the terminal where the server is running.

## License
This project is licensed under the MIT License.

