""" This module is used to get insights from an audio file using regex patterns. """
from find_text import find_insights
from transcribe import transcribe_audio_file


def get_insights_from_audio_url_using_regex(url, regex_patterns):
    """Get insights from an audio URL using regex patterns"""
    transcribed_text = transcribe_audio_file(url)
    return find_insights(transcribed_text, regex_patterns)
