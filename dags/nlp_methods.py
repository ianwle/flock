import re
import pandas as pd
import nltk

from nltk import word_tokenize
from spellchecker import spellchecker
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import word_tokenize, pos_tag

# NLTK Corpii downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

ENGLISH_STOPWORDS = stopwords.words('english')

def to_lowercase(text: str) -> str:
    return str(text).lower()

def to_no_whitespace(text: str) -> str:
    return " ".join(text.split())

def to_tokens(text: str) -> list[str]:
    return word_tokenize(text)

def to_correct_spelling(text: list[str]) -> list[str]:
    result = []
    spell = spellchecker.SpellChecker()
    
    for word in text:
        correct_word = spell.correction(word)
        result.append(correct_word)
        
    return result

def to_no_stopwords(text: str) -> list[str]:
    result = []
    for token in text:
        if token not in ENGLISH_STOPWORDS:
            result.append(token)
    return result

def to_no_punctuation(text: list[str]) -> list[str]:
    tokenizer = RegexpTokenizer(r"\w+")
    result = tokenizer.tokenize(' '.join(text))
    return result

def to_lemmatized(text: list[str]) -> list[str]:
    result = []
    
    wordnet = WordNetLemmatizer()
    for token, tag in pos_tag(text):
        pos = tag[0].lower()
        
        if pos not in ['a', 'r', 'n', 'v']:
            pos = 'n'
        
        result.append(wordnet.lemmatize(token, pos))
    
    return result

def to_stemmed(text):
    porter = PorterStemmer()
    
    result = []
    
    for word in text:
        result.append(porter.stem(word))
        
    return result

def to_no_tags(text):
    text = ' '.join(text)
    html_pattern = re.compile("<.*?>")
    return html_pattern.sub(r'', text)

def to_no_url(text):
    url_pattern = re.compile(r"https?://\S+|www\.\S+")
    return url_pattern.sub(r'', text)

def to_clean_tokens(text):
    return to_stemmed(to_lemmatized(to_no_stopwords(to_correct_spelling(to_no_punctuation(to_tokens(to_no_whitespace(to_lowercase(text))))))))

def to_clean_text(text):
    return " ".join(to_clean_tokens(text))
    