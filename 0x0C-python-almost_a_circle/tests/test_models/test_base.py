#!/usr/bin/python3
""" Test cases for base module"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Test cases for base module"""

    def test_doc(self):
        """Test documentation"""
        self.assertIsNotNone(Base.__doc__)
        self.assertGreater(len(Base.__doc__), 1)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertGreater(len(Base.__init__.__doc__), 1)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertGreater(len(Base.to_json_string.__doc__), 1)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertGreater(len(Base.from_json_string.__doc__), 1)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertGreater(len(Base.save_to_file.__doc__), 1)

    def test_base(self):
        """Test base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{'x': 1}]), '[{"x": 1}]')
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        """Test from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"x": 1}]'), [{'x': 1}])
        with self.assertRaises(TypeError):
            Base.from_json_string()


if __name__ == "__main__":
    unittest.main()
