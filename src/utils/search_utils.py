""" This module contains utility functions for searching text data """

def find_index(sent, char_index):
    """Find the index of the word in a sentence that contains a given character index"""
    word_index = -1
    for i, token in enumerate(sent):
        char_start = token.idx
        char_end = char_start + len(token.text)

        if char_start <= char_index < char_end:
            word_index = i
            break
    return word_index
