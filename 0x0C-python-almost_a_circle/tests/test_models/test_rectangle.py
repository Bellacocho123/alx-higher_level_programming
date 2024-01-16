#!/usr/bin/python3
""" written tests for rectangle object """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """

    class to test rectangle

    """

    def test_attributes(self):
        """ testing attributes """
        r = Rectangle(5, 10)
        self.assertIsInstance(r.width, int)
        self.assertIsInstance(r.height, int)
        self.assertIsInstance(r.x, int)
        self.assertIsInstance(r.y, int)
        self.assertIsInstance(r.id, int)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def testing_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        """
        check raise exception

        r4 = Rectangle("a", 10)
        self.assertRaises(ValueError, r4.id)
        """

    def test_invalid_width(self):
        """Test invalid width value """
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_invalid_height(self):
        """ Test invalid width value """
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_str_method(self):
        """ Test the __str__ method """
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_area_method(self):
        """ Test the area method """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_update_method(self):
        """ Test the update method """
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(2, 8, 12, 4, 6)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)
        self.assertEqual(r.id, 2)


    def test_to_dictionary_method(self):
        """ Test the to_dictionary method """
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(r.to_dictionary(), expected_dict)
