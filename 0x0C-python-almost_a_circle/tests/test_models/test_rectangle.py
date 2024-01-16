#!/usr/bin/python3

"""Test cases for rectangle module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ Test cases for rectangle module"""

    def test_doc(self):
        """Test documentation"""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertGreater(len(Rectangle.__doc__), 1)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)

    def test_rectangle_instance(self):
        """Test Rectangle is a subclass of Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_attributes(self):
        """Test Rectangle attributes"""
        s1 = Rectangle(10, 2)
        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))

    def test_rectangle_attributes(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 12)

    def test_method_has_doc(self):
        """Test if methods have documentation"""
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_rectangle_width(self):
        """Test width setter and getter"""
        r1 = Rectangle(10, 2)
        r1.width = 20
        self.assertEqual(r1.width, 20)
        with self.assertRaises(TypeError):
            r1.width = "2"
        with self.assertRaises(ValueError):
            r1.width = -10

    def test_rectangle_height(self):
        """Test height setter and getter"""
        r1 = Rectangle(10, 2)
        r1.height = 20
        self.assertEqual(r1.height, 20)
        with self.assertRaises(TypeError):
            r1.height = "2"
        with self.assertRaises(ValueError):
            r1.height = -10

    def test_rectangle_x(self):
        """Test x setter and getter"""
        r1 = Rectangle(10, 2)
        r1.x = 20
        self.assertEqual(r1.x, 20)
        with self.assertRaises(TypeError):
            r1.x = "2"
        with self.assertRaises(ValueError):
            r1.x = -10

    def test_rectangle_y(self):
        """Test y setter and getter"""
        r1 = Rectangle(10, 2)
        r1.y = 20
        self.assertEqual(r1.y, 20)
        with self.assertRaises(TypeError):
            r1.y = "2"
        with self.assertRaises(ValueError):
            r1.y = -10

    def test_rectangle_area(self):
        """Test area method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_rectangle_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update(self):
        """Test update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 6,
                         'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (6) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
