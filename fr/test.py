import unittest
from yali.fr.synonyms import Crisco

class TestSynonyms(unittest.TestCase):

	def setUp(self):
		self.crisco = Crisco()
		self.word = 'nettoyer'

	def test_synonyms_of(self):
		synonyms = list(self.crisco.synonyms_of(self.word))
		self.assertIn("frotter", synonyms)

	def test_antonyms_of(self):
		antonyms = list(self.crisco.antonyms_of(self.word))
		self.assertIn('salir', antonyms)

if __name__ == '__main__':
    unittest.main()