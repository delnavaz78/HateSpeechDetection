# python -c "import sys; sys.path.insert(0, 'src'); from hate_speech.preprocessing import clean_text; print(clean_text('Hello @user, check https://example.com 123!'))"



import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to map POS tags to the format used by WordNetLemmatizer
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def clean_text(text):
    # Normalize text
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'@\S+', '', text)  # Remove mentions
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    text = re.sub(r'http\S+', '', text)  # Remove URLs from the tweet
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters (there are emojis in some tweets)

    # Tokenize and lemmatize
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens]

    return ' '.join(tokens)

