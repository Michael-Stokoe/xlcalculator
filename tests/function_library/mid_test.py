
import unittest

import pandas as pd

from koala_xlcalculator.function_library import Mid
from koala_xlcalculator.exceptions import ExcelError


class Test_Mid(unittest.TestCase):
    def test_start_num_must_be_integer(self):
        with self.assertRaises(ExcelError):
            Mid.mid('Romain', 1.1, 2)

    def test_num_chars_must_be_integer(self):
        with self.assertRaises(ExcelError):
            Mid.mid('Romain', 1, 2.1)

    def test_start_num_must_be_superior_or_equal_to_1(self):
        with self.assertRaises(ExcelError):
            Mid.mid('Romain', 0, 3)

    def test_num_chars_must_be_positive(self):
        with self.assertRaises(ExcelError):
            Mid.mid('Romain', 1, -1)

    def test_mid(self):
        self.assertEqual(Mid.mid('Romain', 3, 4), 'main')
        self.assertEqual(Mid.mid('Romain', 1, 2), 'Ro')
        self.assertEqual(Mid.mid('Romain', 3, 6), 'main')
