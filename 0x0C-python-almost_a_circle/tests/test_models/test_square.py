#!/usr/bin/python3
"""Test cases for square module"""""


import unittest
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):
    """ Test cases for square module"""

    def test_doc(self):
        """Test documentation"""
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)

    def test_doc_length(self):
        """ Doc length """
        self.assertGreater(len(Square.__doc__), 1)
        self.assertGreater(len(Square.__init__.__doc__), 1)

    def test_square_instance(self):
        """Test Square is a subclass of Rectangle class"""
        self.assertTrue(isinstance(Square(1), Rectangle))

    def test_square_instance_base(self):
        """Test Square is a subclass of Base class"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_attributes(self):
        """Test Square attributes"""
        s1 = Square(1)
        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "size"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))

    def test_str_method(self):
        """Test __str__ method"""
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")

    def test_size(self):
        """Test size setter and getter"""
        s1 = Square(1)
        s1.size = 2
        self.assertEqual(s1.size, 2)
        with self.assertRaises(TypeError):
            s1.size = "2"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_update(self):
        """Test update method"""
        s1 = Square(1, 2, 3, 4)
        s1.update(10, 20, 30, 40)
        self.assertEqual(s1.__str__(), "[Square] (10) 30/40 - 20")
        s1.update(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(id=10, size=20, x=30, y=40)
        self.assertEqual(s1.__str__(), "[Square] (10) 30/40 - 20")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 3, 'id': 4, 'size': 1})
        self.assertTrue(type(s1_dictionary) is dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)
        self.assertFalse(s1 is s2)


if __name__ == "__main__":
    unittest.main()
