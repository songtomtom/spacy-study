import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Define patterns
pattern1 = [{"POS": "VERB"}, {"POS": "ADV"}]  # Verb followed by adverb
pattern2 = [{"POS": "VERB"}, {"POS": "ADP"}]  # Verb followed by preposition
pattern3 = [{"POS": "VERB"}, {"POS": "ADV"}, {"POS": "ADP"}]  # Verb followed by adverb and preposition

# Add patterns to the matcher
matcher.add('VERB_ADV', [pattern1])
matcher.add('VERB_ADP', [pattern2])
matcher.add('VERB_ADV_ADP', [pattern3])

texts = [
    "Despite the hardships and challenges, he did not give up on his dreams.",
    "The sun rises up in the east and sets down in the west.",
    "He climbed up the stairs to reach the rooftop terrace.",
    "I'm up for whatever.",
    "There are flights to Seoul.",
    "He tends to worry too much about the small details.",
    "I waited about for an hour, but they didn't come.",
    "They enter into an agreement with their rivals.",
    "Could you put me through to extension 259 please."
]

for text in texts:
    print(f'Analysing "{text}"')
    doc = nlp(text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        matched_span = doc[start:end]
        print('- Found match: "', matched_span.text, '" for pattern', nlp.vocab.strings[match_id])
    print()
