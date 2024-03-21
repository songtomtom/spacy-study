import spacy
from spacy.matcher import Matcher

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize the Matcher
matcher = Matcher(nlp.vocab)

# Define patterns allowing for a noun or pronoun
# These patterns are the same as before, intended to capture verb phrases possibly including nouns or pronouns
verb_noun_or_pron_adv_pattern = [{"POS": "VERB"}, {"POS": "NOUN", "OP": "?"}, {"POS": "PRON", "OP": "?"},
                                 {"POS": "ADV"}]
verb_noun_or_pron_adp_pattern = [{"POS": "VERB"}, {"POS": "NOUN", "OP": "?"}, {"POS": "PRON", "OP": "?"},
                                 {"POS": "ADP"}]
verb_noun_or_pron_adv_adp_pattern = [{"POS": "VERB"}, {"POS": "NOUN", "OP": "?"}, {"POS": "PRON", "OP": "?"},
                                     {"POS": "ADV"}, {"POS": "ADP"}]

# Add patterns to the matcher
matcher.add("VERB_NOUN_OR_PRON_ADV", [verb_noun_or_pron_adv_pattern])
matcher.add("VERB_NOUN_OR_PRON_ADP", [verb_noun_or_pron_adp_pattern])
matcher.add("VERB_NOUN_OR_PRON_ADV_ADP", [verb_noun_or_pron_adv_adp_pattern])

# Sample texts
texts = ["Despite the hardships and challenges, he did not give up on his dreams.",
         "The sun rises up in the east and sets down in the west.",
         "He climbed up the stairs to reach the rooftop terrace.",
         "I'm up for whatever.",
         "There are flights to Seoul.",
         "He tends to worry too much about the small details.",
         "I waited about for an hour, but they didn't come.",
         "They enter into an agreement with their rivals.",
         "Could you put me through to extension 259 please.",
         "I've booked us into a hotel in the centre of town for three nights.",
         "I'll book us in at the Intercontinental."]


# Process each text and find matches
for text in texts:
    doc = nlp(text)
    lemmatized_sentence = " ".join([token.lemma_ for token in doc])
    print(f"Sentence: '{lemmatized_sentence}'")

    lemmatized_doc = nlp(lemmatized_sentence)
    matches = matcher(lemmatized_doc)

    # Collect all extracted phrasal verbs
    phrasal_verbs = []
    for match_id, start, end in matches:
        verb_phrase = ' '.join(token.text for token in lemmatized_doc[start:end] if token.pos_ in ['VERB', 'ADV', 'ADP'])
        phrasal_verbs.append((start, verb_phrase))

    # Combine overlapping phrasal verbs
    combined_phrasal_verbs = []
    phrasal_verbs = sorted(phrasal_verbs, key=lambda x: x[0])
    for i in range(len(phrasal_verbs)):
        if i + 1 < len(phrasal_verbs) and phrasal_verbs[i][1] in phrasal_verbs[i + 1][1]:
            # Skip adding the shorter verb phrase when it's part of the next one
            continue
        combined_phrasal_verbs.append(phrasal_verbs[i][1])

    # Print the results
    for verb_phrase in combined_phrasal_verbs:
        print(f" - Extracted phrasal verb: {verb_phrase}")
