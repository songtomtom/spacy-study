import spacy
from spacy.matcher import Matcher

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the Matcher
matcher = Matcher(nlp.vocab)

# Define patterns for phrasal verbs
verb_adv_pattern = [{"POS": "VERB"}, {"POS": "ADV"}]  # Verb followed by an adverb
verb_adp_pattern = [{"POS": "VERB"}, {"POS": "ADP"}]  # Verb followed by a preposition
verb_adv_adp_pattern = [{"POS": "VERB"}, {"POS": "ADV"}, {"POS": "ADP"}]  # Verb followed by an adverb then a preposition

# Add patterns to the matcher
matcher.add("VERB_ADV", [verb_adv_pattern])
matcher.add("VERB_ADP", [verb_adp_pattern])
matcher.add("VERB_ADV_ADP", [verb_adv_adp_pattern])

# Sample texts
texts = ["Despite the hardships and challenges, he did not give up on his dreams.",
         "The sun rises up in the east and sets down in the west.",
         "He climbed up the stairs to reach the rooftop terrace.",
         "I'm up for whatever.",
         "There are flights to Seoul.",
         "He tends to worry too much about the small details.",
         "I waited about for an hour, but they didn't come.",
         "They enter into an agreement with their rivals.",
         "Could you put me through to extension 259 please."]

# Process each text, lemmatize, and find matches in the lemmatized context
for text in texts:
    # Lemmatize the text
    doc = nlp(text)
    lemmatized_sentence = " ".join([token.lemma_ for token in doc])

    # Re-analyze the lemmatized sentence
    lemmatized_doc = nlp(lemmatized_sentence)

    # Find matches
    matches = matcher(lemmatized_doc)
    print(f"Matches in: '{lemmatized_sentence}'")
    for match_id, start, end in matches:
        span = lemmatized_doc[start:end]
        print(f" - Matched: {span.text}")
