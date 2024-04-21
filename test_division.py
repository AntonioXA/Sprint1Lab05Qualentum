import unittest
from division import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-10, 5), -2)
        self.assertEqual(dividir(0, 1), 0)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(6, 0)

if __name__ == '__main__':
    unittest.main()
