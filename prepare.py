#imports
import unicodedata
import re
import json
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

def clean(text):
    'A simple function to cleanup text data'
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') 
    text = (unicodedata.normalize('NFKD', text)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', text).split()
    # Return a joined string
    return " ".join([wnl.lemmatize(word) for word in words if word not in stopwords])

def split(df, stratify_by=None):
    """
    3 way split for train, validate, and test datasets
    To stratify, send in a column name
    """
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
    
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test

def basic_clean(text):
    '''
    This function takes in a string and normalizes it by lowercasing
    everything and replacing anything that is not a letter, number, 
    whitespace or a single quote.
    '''
    
    #lowercase all letters in the text
    text = text.lower()
    
    # normalize unicode by encoding into ASCII (ignore non-ASCII characters)
    # then decoding back into unicode 
    text = unicodedata.normalize('NFKD', text)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')

    # remove any that is not a letter, number, single quote, or whitespace
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    
    return text

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def tokenize(text):
    '''
    This function takes in a string and returns the string will the
    words tokenized
    '''

    # Create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()

    # Use the tokenizer
    text = tokenizer.tokenize(text, return_str=True)
    
    return text   


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def stem(text):
    '''
    This function takes in a string and returns the string after applying
    stemming to all the words.
    '''

    # Create the porter stemmer
    ps = nltk.porter.PorterStemmer()

    # Apply the stemmer to each word in our string.
    stems = [ps.stem(word) for word in text.split()]
    
    # Join our lists of words into a string again
    text_stemmed = ' '.join(stems)

    return text_stemmed


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def lemmatize(text):
    '''
    This function takes in a string and returns the string after applying
    lemmatization to all the words.
    '''

    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()

    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in text.split()]

    # Join our list of words into a string again; assign to a variable to save changes.
    text_lemmatized = ' '.join(lemmas)
    
    return text_lemmatized

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def remove_stopwords(text, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string and optional lists of extra_words and 
    words to exclude from the list and then returns the string after removing stop_words
    '''

    # Define the stop word list
    stopword_list = stopwords.words('english')

    # add extra_words (if any) to the stopwords list
    if len(extra_words) > 0:
        stopword_list = stopword_list.append(extra_words)
      
    # remove exclude_words (if any) from the stopwords list
    if len(exclude_words) > 0:
        stopword_list = stopword_list.remove(exclude_words)   

    # Split words in text.
    text = text.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in text if word not in stopword_list]
    
    # Join words in the list back into strings; assign to a variable to keep changes.
    text_without_stopwords = ' '.join(filtered_words)

    return text_without_stopwords



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prep_article_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)\
                            .apply(lemmatize)
    
    df['stemmed'] = df[column].apply(basic_clean).apply(stem)
    
    df['lemmatized'] = df[column].apply(basic_clean).apply(lemmatize)
    
    return df[['title', column, 'stemmed', 'lemmatized', 'clean']]


