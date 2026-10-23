import unittest
from Calories import Calories

class TestWeightBfSign(unittest.TestCase):
    def test_bothpositive(self):
        kcal = Calories(7,"lb",190,1000,2000,3500)
        self.assertTrue(kcal.WeightChange() > 0 and kcal.Bodyfat() > 0)

    def test_bothnegative(self):
        kcal = Calories(7,"lb",190,1000,2000,2500)
        self.assertTrue(kcal.WeightChange() < 0 and kcal.Bodyfat() < 0)

class TestBf(unittest.TestCase):
    def test_overzero(self):
        kcal = Calories(7,"lb",190,1000,2000,3500)
        self.assertGreaterEqual(kcal.Bodyfat(), 0)

    def test_lesshundred(self):
        kcal = Calories(7,"lb",190,1000,2000,3500)
        self.assertLessEqual(kcal.Bodyfat(), 100)


class TestBodyWeight(unittest.TestCase):
    def test_kg(self):
        kcallb = Calories(7,"lb",190,1000,2000,3500)
        kcalkg = Calories(7,"kg",190,1000,2000,3500)
        self.assertEqual(kcalkg.WeightChange(), kcallb.WeightChange() / 2.20462)

if __name__ == '__main__':
    unittest.main()
