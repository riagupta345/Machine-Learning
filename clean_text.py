from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import sys

# Init objects
tokenizer = RegexpTokenizer(r'\w+')     # To extract all words: r => stands for regular expression, w => all words
en_stopwords = set(stopwords.words('english'))
ss = SnowballStemmer('english')


def clean_review(review):
    review = review.lower()
    review = review.replace("<br />", " ")
    
    words = tokenizer.tokenize(review)
    filtered_words = [word for word in words if word not in en_stopwords]
    stemmed_words = [ss.stem(word) for word in filtered_words]
    
    cleaned_review = ' '.join(stemmed_words)
    return cleaned_review