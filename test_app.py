import unittest

def soma(a, b):
    return a + b

class TestApp(unittest.TestCase):

    def test_soma_1(self):
        self.assertEqual(soma(1, 2), 3)

    def test_soma_2(self):
        self.assertEqual(soma(0, 0), 0)

    def test_soma_3(self):
        self.assertEqual(soma(-1, 1), 0)

    def test_soma_4(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5(self):
        self.assertNotEqual(soma(2, 2), 5)

if __name__ == "__main__":
    unittest.main()
