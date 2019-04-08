import sportifTest
import unittest

class SportTest(unittest.TestCase):

	def test_SizeNegativ(self):
		self.assertRaises(sportif.InvalidSizeError, sportif.Wife, -3, "Foot", "Gru")

	def test_TypeSize(self):
		self.assertRaises(sportif.NotIntegerError, sportif.Wife, "1m", "Foot", "Gru")

	def test_PoidsNegativ(self):
		self.assertRaises(sportif.WeightError, sportif.Athlete, -1)

	def test_Gros(self):
		self.assertRaises(sportif.TooLarge, sportif.Athlete, 205)

if __name__ == "__main__":
    unittest.main()

