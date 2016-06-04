import unittest
from app.calculate import Calculate


class TestExample(unittest.TestCase):
    """
    Here are a bunch of examples which relate to the Unit Test Methods section
    of Chapter 2.  They show the majority of Unittest methods that you are likely
    to make use and you can run the tests by executing the following in the shell
    at the root directory of the project.

    $ python test/examples_test.py
    """

    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1, 1.00001, places=4)

    def test_assert_raises_in_line_style(self):
        self.assertRaises(IndexError, [].pop, 0)

    def test_assert_raises_as_context_manager(self):
        with self.assertRaises(AttributeError):
            [].get

    def test_assert_dict_contains_subset(self):
        actual = {'a': 'b', 'c': 'd', 'e': 'f'}
        self.assertDictContainsSubset({'a': 'b'}, actual)

    def test_assert_dict_equal(self):
        expected = {'a': 'b', 'c': 'd'}
        actual = {'c': 'd', 'a': 'b'}
        self.assertDictEqual(expected, actual)

    def test_assert_true(self):
        self.assertTrue(1)
        self.assertTrue("Hello, World")

    def test_assert_false(self):
        self.assertFalse(0)
        self.assertFalse("")

    def test_assert_greater(self):
        self.assertGreater(2, 1)

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(2, 2)

    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3, 4, 5])

    def test_assert_is(self):
        self.assertIs("a", "a")

    def test_assert_is_instance(self):
        self.assertIsInstance(1, int)

    def test_assert_not_is_instance(self):
        self.assertNotIsInstance(1, str)

    def test_assert_is_none(self):
        self.assertIsNone(None)

    def test_assert_is_not(self):
        self.assertIsNot([], [])

    def test_assert_is_not_none(self):
        self.assertIsNotNone(1)

    def test_assert_less(self):
        self.assertLess(1, 2)

    def test_assert_less_equal(self):
        self.assertLessEqual(2, 2)

    def test_assert_items_equal(self):
        self.assertItemsEqual([1, 2, 3], [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
