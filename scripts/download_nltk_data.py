"""One-time download of NLTK corpora needed by hate_speech.preprocessing."""
import nltk

REQUIRED_PACKAGES = ['stopwords', 
                     'punkt', 
                     'wordnet',
                     'punkt_tab',
                     'averaged_perceptron_tagger',
                     'omw-1.4',
                     'averaged_perceptron_tagger_eng']


def main() -> None:
    for package in REQUIRED_PACKAGES:
        nltk.download(package)

if __name__ == '__main__':
    main()