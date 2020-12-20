import pickle
import re
import sklearn
import ast
import praw
import joblib
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer

#to avoid redownloading or tedious searching for nltk corpus
#with open('stopwords.txt', 'r') as f:
#    stop_words = ast.literal_eval(f.read())
    
#OR
STOP_WORDS = set(stopwords.words('english'))

#import the model 
model = joblib.load('final_model.sav')

#get reddit data
#Details gotten from the developers applications page
reddit = praw.Reddit(client_id='Jh_3OIHI20MPfw',
                     client_secret='j19OgLGN3tWxA0e9KLoDV1ORfqaC3Q',
                     user_agent='script by daniel Adama',username='danieltovia')
#Data cleaning tools
#Cleaning both text & URL
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
#Cleaning both text & URL
def cleaning(text):
    text = str(text).lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text) #replace REPLACE_BY_SPACE_RE by space in text
    text = BAD_SYMBOLS_RE.sub('', text) #delete symbols which are in BAD_SYMBOLS_RE from text
    # text = text.replace('www', ' ')
    # text = text.replace('com', ' ')
    # text = text.replace('https', ' ')
    text = ' '.join(word for word in text.split() if word not in STOP_WORDS and word.isalpha())
    return text
    
#prediction for a single entry
def get_flair(url, loaded_model=model):
    
    #collect the data from that URL
    submission = reddit.submission(url=url)
    reddit_entry = {}
    
    reddit_entry['Title'] = submission.title
    reddit_entry['URL'] = submission.url
    
    submission.comments.replace_more(limit=0)
    comment = ''
    for top_comments in submission.comments:
        comment = comment + ' ' + str(top_comments.body)
    
    reddit_entry['comment'] = comment
    reddit_entry['sign_features'] = reddit_entry['Title'] + reddit_entry['comment']
    reddit_entry['sign_features'] = cleaning(reddit_entry['sign_features'])
    
#    convert it to a count vectorizer object
#    create an instance of the count vectorizer
    # vect = CountVectorizer()
    # data_count = vect.transform([reddit_entry['Title']])
    
    
    return loaded_model.predict([reddit_entry['sign_features']])
