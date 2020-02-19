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
    This functions takes a date and converts it into a certain format.
    """
    
    date = [datetime.split(' ')[0] for datetime in dates]
    return date


def extract_municipality_hashtags(df):
    
    """
    Modify input dataframe to include two new columns:

        1. column containing the name of the municipality at which the tweet is directed
        2. column containing all of the hashtags of the tweet in another column
    
    Args:
        df (pandas dataframe): dataframe to be modified
    
    Returns:
        pandas dataframe : returns modified dataframe with 'minucipality' and 'hashtag'column added
             
    """
    
    # initialise empty columns to be filled

    df['minucipality'] = ''
    df['hashtag'] = ''

    for tweet_index in range(len(df['Tweets'])): # loop through every row in the tweet column

      hashtags = [] #temp list to hold hashtags for the current tweet

      for word in mun_dict: # loop through every word in mun_dict dictionary
        if word in df['Tweets'][tweet_index]: 
          df['minucipality'][tweet_index] = mun_dict[word] # add municipality name to 'municipality' column if it can be found in the dictionary
        else:
          df['minucipality'][tweet_index] = np.nan 
      
      for word2 in df['Tweets'][tweet_index].lower().split(): # loop through every word in current tweet in 'Tweets' column
        if word2.startswith('#') == True: # add hashtags to temp list
          hashtags.append(word2)
        else:
          pass
      
      df['hashtag'][tweet_index] = hashtags # add temp hashtag list to 'hashtag' column
      
      if len(hashtags) == 0:
        df['hashtag'][tweet_index] = np.nan
        
    return df



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
    


def five_num_summary(items):

    """
    This function return a dictinary of the five number summary.
    """