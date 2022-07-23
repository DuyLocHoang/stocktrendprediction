import pandas as pd 
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


df = pd.read_csv('Data_merged.csv',index_col = 0)
stop_words = set(stopwords.words('english'))
title = []
df["pre"] = df.title.replace("[^a-zA-Z]","",regex=True)
for i in df["pre"] :
    word_tokens = word_tokenize(i)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words and len(w)>1]
    filtered_sentence = ' '.join(filtered_sentence)
    title.append(filtered_sentence)
df = df.drop('pre',axis='columns')
df['pre_title'] = title
df.to_csv('preprocess_data.csv')
