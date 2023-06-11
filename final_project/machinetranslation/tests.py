"""
This module containes tests for tranlsator.py
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    This class is for the english_to_french  tests
    """
    def test_equal(self):
        """
        This function tests the english_to_french function
        """
        self.assertEqual(english_to_french('Tomorrow'), 'Demain')

    def test_not_equal(self):
        """
        This function tests the english_to_french function
        """
        self.assertNotEqual(english_to_french('Hello'), 'Demain')

class TestFrenchToEnglish(unittest.TestCase):
    """
    This class is for the french_to_english  tests
    """
    def test_equal(self):
        """
        This function tests the french_to_english function
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('demain'), 'tomorrow')

    def test_not_equal(self):
        """
        This function tests the french_to_english function
        """
        self.assertNotEqual(french_to_english('Demain'), 'Hello')

unittest.main()
