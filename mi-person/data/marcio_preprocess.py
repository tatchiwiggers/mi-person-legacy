import string
import pandas as pd
import nltk
from nltk.corpus import stopwords 
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import emoji

def __remove_punctuation(text):
    """
        remove punctuation from text and lower case it
    """
    text = str(text)

    punctuations = string.punctuation
    punctuations += '“'
    punctuations += '’'
    punctuations += '”'
    punctuations += '’'
    punctuations += ' — '
    punctuations += 'â€œ'
    punctuations += 'â€¦'
    punctuations += 'â€'
    punctuations += '€™'
    punctuations += '€'
    punctuations += '™'
    punctuations += '¦'
    punctuations += 'œ'
    punctuations += 'Â'
    punctuations += 'Ã'
    punctuations += '— '
    punctuations += '¶'
    punctuations += '§'
    punctuations += '£'
    punctuations += '©'
    punctuations += 'ª'
    punctuations += '³'

    text = emoji.get_emoji_regexp().sub(u'', text)

    for punctuation in punctuations:
        text = text.replace(punctuation, ' ') 
        #text = text.replace('donald', 'trump')
        #text = text.replace('clinton', 'hillary')
    return text.lower() # lower case

def __remove_numbers(text):
    """
        remove number from text
    """
    text = str(text)

    words_only = ''.join([i for i in text if not i.isdigit()])
    return words_only

def __remove_stopwords(text):
    """
        remove stop words from text
    """
    text = str(text)

    stop_words = stopwords.words('english')
    #stop_words += stopwords.words('portuguese')
    stop_words.append('mr')
    stop_words = set(stop_words)

    tokenized = word_tokenize(text)
    without_stopwords = [word for word in tokenized if not word in stop_words]
    return without_stopwords

def __lemmatize(text):
    """
        lemmatize text
    """
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in text]
    lemmatized_string = " ".join(lemmatized)
    return lemmatized_string


def process_data(df):
    """
        process the data
    """

    df_ = df.copy()
        
    df_['text'] = df_['text'].apply(__remove_punctuation)

    df_['text'] = df_['text'].apply(__remove_numbers)

    df_['text'] = df_['text'].apply(__remove_stopwords)

    df_['text'] = df_['text'].apply(__lemmatize)
    
    return df_