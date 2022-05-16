import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    Load & merge messages and categories 

    inputs:
    messages_filepath
    categories_filepath

    outputs:
    df: containing merge of messagesa and categories
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, left_on='id', right_on='id', how='inner')

    return df

def clean_data(df):
    '''
    Clean df by removing duplicates & converting categories to binary values 

    inputs:
    df: containing merge of messages and categories

    outputs:
    df: containing clean version of input dataframe
    '''
    categories  = df['categories'].str.split(';',expand=True)
    # select the first row of the categories dataframe
    row = categories.iloc[0]
    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    # rename the columns of `categories`
    categories.columns = category_colnames

    for column in categories:
    # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]
    
    # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    # drop the original categories column from `df`
    df.drop(columns=['categories'], inplace = True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], join='inner', axis = 1)

    # Remove rows with a related value of 2 from the dataset
    df = df[df['related'] != 2]

    return df


def save_data(df, database_filename):
    '''Save into Database
    
    inputs:
    df: cleaned dataframe
    database_filename: filename for output database
    '''
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Disaster_Response', engine, index = False, if_exists = 'replace')
    


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()