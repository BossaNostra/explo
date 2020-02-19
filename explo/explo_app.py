import numpy as np
import pandas as pd



def metric_dict(items):

    """
    Write a function that calculates metrics from Eskom Data and outputs the metrics as a dictionary. 
    These metrics must include:
        
    > Mean
    > Median
    > Maximum
    > Minimum
    > Standard Deviation
    > Variance

    """

def date_parser(dates):

    """
    Takes an input Pandas DataFrame with a datetime column of the format(yyyy-mm-dd hh:mm:ss) 
    and modifies it to return just the date in the format (yyyy-mm-dd)
    
    Args:
        df (pandas dataframe): dataframe to be modified
    
    Returns:
        pandas dataframe : with the modified date column
    """
    #Reset the date column with a list comprehension 
    date = [datetime.split(' ')[0] for datetime in dates]
    return date


def extract_municipality_hastags(df):

    """
    This function must return a dataframe with:
    An added column of extracted hashtags from each tweet.
    An added column of the municipality mentioned in each tweet 
    """



def number_of_tweets_per_day(df):
    
    """
    
    Takes an input Pandas DataFrame with a datetime and Tweet columns and returns a dataframe with:

        1. Date column
        2. Tweets count ordered by date
    
    Args:
        df (pandas dataframe): dataframe to be modified
    
    Returns:
        pandas dataframe : with the modified date column and tweets count ordered by date
        
    """
    
    df['Date'] = [entry.split(' ')[0] for entry in df['Date']]
    return df.groupby('Date').count()


def stop_words_remover(df):

    """
    This function returns a dataframe without stop words
    """


def word_splitter(df):

    """
    This function takes a dataframe and returns a new dataframe with 
    a new column of individual words
    """
    


def five_num_summary(items):

    """
    This function return a dictinary of the five number summary.
    """