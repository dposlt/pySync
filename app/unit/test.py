import cases
import unittest

class KnowValues(unittest.TestCase):
    know_values = ((1, 'David'),
                    (2, 'Petr'),
                    (3, 'Monika'),
                    (4, 'Vladka'))

    def test_to_c(self):
        for integer, numeral in self.know_values:
            result = cases.to_roman(integer)
            self.assertEqual(numeral, result)


if __name__ == '__main__':
    unittest.main()

