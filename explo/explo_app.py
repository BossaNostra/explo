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
#I'm testing the shit out of this

def date_parser(dates):

    """
    This functions takes a date and converts it into a certain format.
    """
    
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
    This function returns a number of tweets per day.
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
    df['Split Tweets'] = [tweet.split(' ') for tweet in df['Tweets']]
    return df


def five_num_summary(items):

    """
    This function return a dictinary of the five number summary.
    """