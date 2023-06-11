"""
This module contains several translating functions
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates a English text into French
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates a French text into English
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
