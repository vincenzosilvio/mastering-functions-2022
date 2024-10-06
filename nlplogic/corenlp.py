from textblob import TextBlob
import wikipedia
import nltk

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt_tab")


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching 4 name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """ "Summarize wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """ "Getting text blob object"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """ "Find wikipedia name and return back phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


golden_state_warriors_text = wikipedia.summary("Golden State Warriors")

print(get_phrases("Golden State Warriors"))
