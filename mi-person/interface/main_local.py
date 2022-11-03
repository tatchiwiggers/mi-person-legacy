import string
import pandas as pd


class DataProcessing:
    def __init__(self) -> None:
        self.df = pd.read_csv('../mi-person/data/df_test.csv')


    def load_df(self):
        return self.df


    def __remove_punctuation(self, text):
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


        for punctuation in punctuations:
            text = text.replace(punctuation, ' ') 

        return text.lower() # lower case


    def __remove_numbers(self, text):
        """
            remove number from text
        """
        text = str(text)

        words_only = ''.join([i for i in text if not i.isdigit()])
        return words_only


    def process_data(self, df):
        """
            process the data
        """

        df_ = df.copy()
            
        df_['text'] = df_['text'].apply(self.__remove_punctuation)

        df_['text'] = df_['text'].apply(self.__remove_numbers)
        
        return df_


dp = DataProcessing()
df = dp.load_df()

cleaned_sentences = dp.process_data(df)
cleaned_sentences.shape

print(cleaned_sentences['text'])