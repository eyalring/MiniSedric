"""Find words in a text that match the search patterns using spacy"""
import re
import spacy
from utils.search_utils import find_index


nlp = spacy.load("en_core_web_sm")

def find_insights(text, search_patterns):
    """Find words in a song text that match the search patterns"""
    doc = nlp(text)
    insights_to_return = []

    for sentence_index, sent in enumerate(doc.sents):
        for pattern in search_patterns:
            match = re.search(pattern, sent.text, re.IGNORECASE)
            for match in re.finditer(pattern, sent.text, re.IGNORECASE):
                start_char_idx = match.start() + sent.start_char
                end_char_idx = match.end() + sent.start_char

                start_word_index = find_index(sent, start_char_idx)
                end_word_index = find_index(sent, end_char_idx)


                insights_to_return.append({"sentence_index": sentence_index,
                                           "start_word_index": start_word_index,
                                            "end_word_index": end_word_index,
                                            "tracker_value": pattern,
                                            "transcribe_value": sent.text})

    return insights_to_return
