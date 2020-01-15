import bubble_sort
import unittest


class TestBubbleSort(unittest.TestCase):
    def test_for_one_element(self):
        # stubs
        element_array = [1]

        # action
        result = [1]

        # test
        self.assertEqual(result, bubble_sort.bubbleSort(element_array), "No action should be made")

    def test_for_just_two_element(self):
        # stubs
        element_array = [1, 2]

        # action
        result = [1, 2]

        # test
        self.assertEqual(result, bubble_sort.bubbleSort(element_array), "No action should be made")

    def test_return_value_are_valid(self):
        # stubs
        element_array = [1, 2]

        # action
        result = [1, 2]

        # test
        self.assertIsNotNone(bubble_sort.bubbleSort(element_array), "Return value is not None")

    def test_for_value_return_from_function(self):
        # stubs
        element_array = None

        # action

        # test
        self.assertRaises()

    def test_empty_obj(self):
        # stubs
        element_array = None

        # action

        # test
        self.assertIsNone(bubble_sort.bubbleSort(element_array), "Parameter for function is None")
