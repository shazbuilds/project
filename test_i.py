import unittest
from i import tanlovni_tekshir, ha_yoq


class YordamchiTest(unittest.TestCase):
    def test_tanlov(self):
        self.assertEqual(tanlovni_tekshir("3", 5), 3)
        self.assertIsNone(tanlovni_tekshir("9", 5))
        self.assertIsNone(tanlovni_tekshir("abc", 5))

    def test_ha_yoq(self):
        self.assertTrue(ha_yoq("h"))
        self.assertTrue(ha_yoq(" Ha "))
        self.assertFalse(ha_yoq("y"))


if __name__ == "__main__":
    unittest.main()
