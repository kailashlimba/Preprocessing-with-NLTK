import nltk
import re 
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def preprocessor(text):
    text = re.sub(r'\W+|\d+|_',' ',text)  # removing punctuations and numbers
    text = nltk.word_tokenize(text)        #tokeninzing
    text = [word for word in text if not word in stop_words] # english stop words
    text = [lemmatizer.lemmatize(word) for word in text]
    return text