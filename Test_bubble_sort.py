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
