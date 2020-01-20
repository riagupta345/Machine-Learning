# Creating an NLP pipeline to clean review data
# - Load input file and read reviews
# - Tokenize
# - Remove stopwords
# - Perform stemming
# - Write clean data to output file


review1 = """I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. 
				It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disaster, 
				nudity/sexuality and some language."""
# print(review1)

# NLTK modules
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

# Function to accept input file and write to cleaned output file
def clean_document(inputFile, outputFile):
	out = open(outputFile, 'w')

	with open(inputFile) as f:
		reviews = f.readlines()	

	for review in reviews:
		cleaned_review = clean_review(review)
		print(cleaned_review, file = out)        # Writing to output file

	out.close()

inputFile = sys.argv[1]
outputFile = sys.argv[2]
clean_document(inputFile, outputFile)