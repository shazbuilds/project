import unittest
from model import Vazifa
class VazifaTest(unittest.TestCase):
    def test_yangi_vazifa(self):
        v = Vazifa("Dars qilish")
        self.assertFalse(v.bajarildi)

    def test_bajar(self):
        v = Vazifa("Dars qilish")
        v.bajar()
        self.assertTrue(v.bajarildi)

    def test_bosh_matn(self):
        with self.assertRaises(ValueError):
            Vazifa("   ")