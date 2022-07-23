import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

def remove_non_ascii_chars(text):
    return ''.join([w if ord(w) < 128 else ' ' for w in text])


def preprocessing(headline):

    headline = remove_non_ascii_chars(headline)
    print(headline)
    word_tokens = word_tokenize(headline)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words and len(w)>1]
    filtered_sentence = ' '.join(filtered_sentence)
    print(filtered_sentence)
    return filtered_sentence

if __name__ == "__main__":
    preprocessing("Buckingham 5 Research Initiates Coverage on T-Mobile US at Buy, Announces $50.00 PT")