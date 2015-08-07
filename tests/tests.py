import unittest
import sys

sys.path.append('..')
from db.fields import numbers, orm


class TestSqlConstruction(unittest.TestCase):
    
    def test_simple(self):
        self.a = numbers.IntField(maximum=200)
        self.assertEqual(self.a.sql('width'), 'integer CHECK (width<200)')

    def test_one_to_one(self):
        class OneClass(object):
            potato = 'Potato'
        onetoone = orm.OneToOne(OneClass, required=True)
        self.assertEqual(onetoone.sql(), 'OneClass_id integer NOT NULL REFERENCES OneClass')


if __name__ == '__main__':
    unittest.main()
