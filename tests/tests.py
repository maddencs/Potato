import unittest
import sys

sys.path.append('..')
from fields import numbers


class TestSqlConstruction(unittest.TestCase):
    
    def test_simple(self):
        self.a = numbers.IntField(maximum=200)
        self.assertEqual(self.a.sql('width'), 'integer CHECK (width<200)')


if __name__ == '__main__':
    unittest.main()
