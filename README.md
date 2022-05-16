# Disaster Response Pipeline Project
Description:
This project is an effort to classify disaster messages during times of emergency. This dataset was obtained by Figure Eigth.

The Project is divided into the following Sections:

Data Processing, ETL Pipeline to extract data from source, clean data and save them in a proper databse structure.
Machine Learning Pipeline to train a model which is able to classify text messages in 36 categories.
Web Application using Flask to show model results and predictions in real time.
Data:

This dataset contains 30,000 messages drawn from events including an earthquake in Haiti in 2010, an earthquake in Chile in 2010, floods in Pakistan in 2010, super-storm Sandy in the U.S.A. in 2012, and news articles spanning a large number of years and 100s of different disasters.

The data has been encoded with 36 different categories related to disaster response and has been stripped of messages with sensitive information in their entirety.

Data includes 2 csv files:

disaster_messages.csv: Messages data.
disaster_categories.csv: Disaster categories of messages.
Folder Structure:
app

| - templates
|- master.html # main page of web application
|- go.html # classification result page of web application
|- run.py # Flask file that runs application
data

|- disaster_categories.csv # data to process
|- ML Pipeline Preparation.ipynb
|- ETL Pipeline Preparation.ipynb
|- disaster_messages.csv # data to process
|- process_data.py
|- Disaster_Response.db # database to save clean data to
models

|- train_classifier.py
|- classifier.pkl # saved model
README.md

Installation:
This project requires Python 3.x and the following Python libraries:

Machine Learning Libraries: NumPy, SciPy, Pandas, Sciki-Learn
Natural Language Process Libraries: NLTK
SQLlite Database Libraqries: SQLalchemy
Web App and Data Visualization: Flask, Plotly


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
