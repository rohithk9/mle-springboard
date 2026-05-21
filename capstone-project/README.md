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
  - rec_app.py
  - beer_recommender_model.pkl
  - requirements.txt
  - chatbot.html

## Prerequisites
Before running the application, ensure that you have the following installed on your local machine:

 - Python 3.7 or above
 - pip (Python package installer)
 - Flask and other required libraries (specified in requirements.txt)

## Getting Started
1. Clone the repository

  ```bash
  git clone https://github.com/rohithk9/mle-springboard.git
  cd mle-springboard/capstone-project/recommender-app
  ```

2. Set up a virtual environment (optional)

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

  The `requirements.txt` file includes the official OpenAI Python package as `openai`.

4. Configure your OpenAI API key

  Create a `.env` file in `recommender-app/` with:

  ```text
  OPENAI_API_KEY=sk-...
  ```

5. Run the Flask app

  ```bash
  python3 rec_app.py
  ```

6. Edit the chatbot client if needed

  Open `chatbot.html` and verify the backend address used by the client. If the app is running locally, use `http://127.0.0.1:3000` as the backend URL.

7. Open the chatbot interface

  Open `chatbot.html` in your browser. If the browser blocks file-based requests, you can serve the directory with:

  ```bash
  python3 -m http.server 8000
  ```

  Then visit `http://127.0.0.1:8000/chatbot.html`.

8. Stop the Flask app

  Press `Ctrl+C` in the terminal where the Flask server is running.

## License

This project is licensed under the MIT License.
