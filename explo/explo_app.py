import numpy as np
import pandas as pd

"""
Data Loading and Preprocessing
"""
#Electricification by province (EBP) data:
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

#Twitter Data:
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

#Important Variables:

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

'''
Functions
'''

def dictionary_of_metrics(items):

    """
    function calculates the mean,median,variance,standard deviation and also gets minimim and maximum of the data that has been given and has been rounded off to 2 decimal.
    
    Parameters
    ----------
    a: items
        List of integers
    
    Returns
    -------
    c: Dictionary
        Returns a dictionary of the mean,median,unbiased variance,unbiased standard deviation,minimim value, and maximum value of the inputted list.
    """
    
    dic = {'mean': round(np.mean(items),2), 
            'median': round(np.median(items),2), 
            'var': round(np.var(items, ddof=1),2),
            'std': round(np.std(items, ddof=1),2),
            'min': round(np.min(items),2),
            'max': round(np.max(items),2)
           }
    
    return dic

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
        pandas dataframe : returns modified pandas dataframe with 'minucipality' and 'hashtag'column added
             
    """
    
    # initialise empty columns to be filled

    df['municipality'] = ''
    df['hashtags'] = ''

    for tweet_index in range(len(df['Tweets'])): # loop through every row in the tweet column

        hashtags = [] #temp list to hold hashtags for the current tweet

        for word in mun_dict: # loop through every word in mun_dict dictionary
            if word in df['Tweets'][tweet_index]:
                df['municipality'][tweet_index] = mun_dict[word] # add municipality name to 'municipality' column if it can be found in the dictionary
            else:
                df['municipality'][tweet_index] = np.nan 
      
        for word2 in df['Tweets'][tweet_index].lower().split(): # loop through every word in current tweet in 'Tweets' column
            if word2.startswith('#') == True: # add hashtags to temp list
                hashtags.append(word2)
            else:
                pass
      
        df['hashtags'][tweet_index] = hashtags # add temp hashtag list to 'hashtag' column
      
        if len(hashtags) == 0:
            df['hashtags'][tweet_index] = np.nan
        
    return df



def number_of_tweets_per_day(df):
    
    """
    This function returns a number of tweets per day.
    """
    df['Date'] = [entry.split(' ')[0] for entry in df['Date']]
    return df.groupby('Date').count()


def stop_words_remover(df):
    """
    Removes english stop words from a tweet as defined by a dictionary stop_words_dict
    
    Parameters
    ----------

    df: pandas dataframe
    
    Returns
    -------
    df: pandas dataframe
        Modified dataframe with new column 'Without Stop Words' that has lowercased split tweets with all stop words removed

    Examples

    -------
        >> stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"]
        ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
        1        
        >> stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"]
        ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit']
       
  """

    stop_word_list=list(stop_words_dict.values())[0] # created a list from 'stop words' key of stop_word_dict

    remover_df=df.copy() # duplicated DataFrame df as remover_df
  
    remover_df['Without Stop Words']=remover_df['Tweets'].apply(lambda x: x.lower().split()) # generated new column 'Without Stop Words' from column 'Tweets'

  #for loop to interate through every row of column 'Without Stop Words'
    for entry in remover_df['Without Stop Words']:

    # for loop to iterate though every list element on row specified by entry
        for element in entry:

            retry=entry.count(element) #counts number of stop words in row to determine condition for while loop

            while retry>0: 
        
                if element in stop_word_list: # for every stop word in row, the element must be removed from the row
                    entry.remove(element)
                    retry=retry-1
                else:
                    break # if no stop word is found, break loop and continue to next row

    return remover_df


def word_splitter(df):
    
    """
    This Function takes in a dataframe of tweets, creates a copy of the Dataframe, creates a new column,
    and transforms the tweets within, in order to be more readable. 

    Parameters
    -----
    word_splitter = df.copy(deep=True): creates the copy of the dataframe.

    word_splitter['Split Tweets']: The new column that will be added

    df['Tweets'].apply : Is the existing column we wish to manipulate.

    lambda Tweets: Tweets.lower().split(): Is the actual function that performs the transformation we want
    by spilting the tweets into words, and making them lowercase.
    ------
    Returns
    ------
    The new(copied) dataframe with the tweets that have been transformed to be spilt and lowercase.
    """
    
    word_splitter = df.copy(deep=True)
    
    # spilts the sentences in "tweets" to words and makes all words lower case
    word_splitter['Split Tweets']= df['Tweets'].apply(lambda Tweets: Tweets.lower().split())
    
    return word_splitter
    


def five_num_summary(items):
    """
    function calculates the median, and gets minimim and maximum the first percentile and second percentile of the data that has been given and has been rounded off to 2 decimal.
    
    Parameters
    ----------
    a: items
        List of integers
    
    Returns
    -------
    c: Dictionary
        Returns a dictionary of the median,minimim value, maximum value, first percentile and second percentile of the inputted list.
    """
    dic = { 'max': round(np.max(items),2),
             'min': round(np.min(items),2),
             'median': round(np.median(items),2),
              'q1': round(np.percentile(items, 25),2),
               'q3': round(np.percentile(items, 75),2)}
    return dic