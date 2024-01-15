#!/usr/bin/python3
""" written tests for Square subclass """
import io
import sys
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """
    test cases for square
    """

    def test_square(self):
        """ test square method """
        s1 = Square(5)
        self.assertEqual(s1.id, 7)

        s2 = Square(2, 2)

    def test_square_area(self):
        """ testing the return of Area """
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

        """ self.assertEqual(print(s3), '[Square] (3) 1/3 - 3') """

    def test_attributes(self):
        """ Test attribute types and default values """
        s = Square(5, 2, 3, 1)
        self.assertIsInstance(s.size, int)
        self.assertIsInstance(s.x, int)
        self.assertIsInstance(s.y, int)
        self.assertIsInstance(s.id, int)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertIsNotNone(s.id)

    def test_invalid_size(self):
        """ Test invalid size value """
        with self.assertRaises(ValueError):
            Square(-5, 2, 3, 1)

    def test_str_method(self):
        """ Test the __str__ method """
        s = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_size_property(self):
        """ Test the size property """
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        s.size = 8
        self.assertEqual(s.size, 8)

    def test_update_method(self):
        """ Test the update method """
        s = Square(5, 2, 3, 1)
        s.update(2, 8, 4, 6)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)
        self.assertEqual(s.id, 2)

    def test_to_dictionary_method(self):
        """ Test the to_dictionary method """
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)

    def test_update_method_invalid_arguments(self):
        """ Test the update method with invalid arguments """
        s = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError):
            s.update(2, -8, 4, 6)

    def test_update_method_keyword_arguments(self):
        """ Test the update method with keyword arguments """
        s = Square(5, 2, 3, 1)
        s.update(size=8, x=4, y=6)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)
