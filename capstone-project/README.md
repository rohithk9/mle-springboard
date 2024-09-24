# Beer Recommender System

This is a Flask-based application that uses a machine learning model to recommend beers based on user input. The user interacts with the app via an HTML-based chatbot, which collects preferences and displays recommendations. This project was a capstone submission for the springboard machine learning engineering extended studies bootcamp.

 #### Project Documents
  - Project Ideas MLE

    [Google Docs - Project Ideas MLE](https://docs.google.com/document/d/16dTOQjlReelYg2SycdRTSj9UKfdtHicqXO20NKD91jA/)

  - Project Proposal MLE

    [Google Docs - Project Proposal MLE](https://docs.google.com/document/d/1MvCQ7fpR8oWrbDG1ALFfYntaVGEXbF0z2PS159ZPIsE/)

  - MLE Existing Research Survey

    [Google Docs - MLE Existing Research Survey](https://docs.google.com/document/d/1Jme7_gUFBW-t2Y3A83d_ipYVXXr9JKyil-b7FYF2-N0/)

  - Picking a Deployment Method

    [Google Docs - Picking a Deployment Method](https://docs.google.com/document/d/1YMIwHF7KcnQG9M3TPVEU2XhrIJtXRPNysHPoJrcQOIg/)

  - Designing my Deployment Solution Architecture

    [Google Docs - Designing my Deployment Solution Architecture](https://docs.google.com/document/d/10jF2UdMhtCZgUt5l0ruOfxZ0rvItdONa0ma5HIXNkWM/)

 
## Project Structure

recommender-app/
  - /rec_app.py              
  - /beer_recommender_model.pkl 
  - /requirements.txt
  - /chatbot.html            

## Prerequisites
Before running the application, ensure that you have the following installed on your local machine:

 - Python 3.7 or above
 - pip (Python package installer)
 - Flask and other required libraries (specified in requirements.txt)

## Getting Started
1. Clone the Repository
  Clone the repository to your local machine:

  ```git clone https://github.com/rohithk9/mle-springboard.git```
  
  ```cd recommender-app```

2. Set Up a Virtual Environment (optional)
  Set up a virtual environment to keep dependencies isolated:

  ```python3 -m venv venv```
  
  ```source venv/bin/activate```

3. Install Dependencies
  Install the required Python packages using pip and the requirements.txt file:

  ```pip install -r requirements.txt```

4. Run the Flask App
  Run the Flask app locally by executing the following command:

  ```python3 rec_app.py```

5. Edit the chatbot.html
  Before running the html file in your browser, please edit the IP address on line 210 to match your local environments IP. (Eg: 127.0.0.1:3000)

7. Open the Chatbot Interface
  To interact with the chatbot, open the chatbot.html file in your browser. This file sends input to the Flask app and displays beer recommendations based on user preferences.

8. Stop the Flask App
  To stop the Flask server, press Ctrl+C in the terminal where the server is running.

## License
  This project is licensed under the MIT License.

