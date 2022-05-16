# Disaster Response Pipeline Project
Description:
This project is an effort to classify disaster messages during times of emergency. This dataset was obtained by Figure Eigth.

The Project is divided into the following Sections:

Data Processing, 
ETL Pipeline to extract data from source, 
clean data and save them in a proper databse structure.
Machine Learning Pipeline to train a model which is able to classify text messages in 36 categories.
Web Application using Flask to show model results and predictions in real time.

Data:

This dataset contains 30,000 messages comprising of different disasters spanning several years. The data has been encoded with 36 different categories related to disaster response.

![image](https://user-images.githubusercontent.com/52591382/168524250-82ed8eaa-4a55-4955-9008-92014377d067.png)

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
