import bubble_sort
import unittest


class TestBubbleSort(unittest.TestCase):
    def test_for_one_element(self):
        # stubs
        element_array = [1]

        # action
        result = [1]

        # test
        self.assertEqual(result, bubble_sort.bubble_sort(element_array), "No action should be made")

    def test_for_just_two_element(self):
        # stubs
        element_array = [1, 2]

        # action
        result = [1, 2]

        # test
        self.assertEqual(result, bubble_sort.bubble_sort(element_array), "No action should be made")

    def test_return_value_are_valid(self):
        # stubs
        element_array = [1, 2]

        # action
        result = [1, 2]

        # test
        self.assertIsNotNone(bubble_sort.bubble_sort(element_array), "Return value is not None")

    def test_for_value_return_from_function(self):
        # stubs
        element_array = None

        # action
        # test
        self.assertRaises(TypeError, bubble_sort.bubble_sort(element_array))

    def test_empty_obj(self):
        # stubs
        element_array = None

        # action

        # test
        self.assertIsNone(bubble_sort.bubble_sort(element_array), "Parameter for function is None")

    def test_for_loss_values(self):
        # stubs
        element_array = [9, 4, 3, 2, 5, 6, 14, 0, 4, 3, 5, 7, 4, 4, ]

        # action
        result = [0, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 9, 14]
        # test
        self.assertEqual(result, bubble_sort.bubble_sort(element_array), "array of integers")

    def test_sort_letters(self):
        # stubs
        element_array = ['x', 't', 'b', 'a', 'd', 'c', ]

        # action
        result = ['a', 'b', 'c', 'd', 't', 'x']
        # test
        self.assertEqual(result, bubble_sort.bubble_sort(element_array), "array of letters")
