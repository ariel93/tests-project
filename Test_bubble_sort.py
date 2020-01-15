import unittest
import bubble_sort


class BubbleSortTest(unittest.TestCase):



    def testAnyValue(self):
        """
        tests if the bubblesort returns any value
        """
        #mock
        mk1 = [767,554,-1,4,554,767,554,14]
        mk2 = [7671, -554554, 1767, 0, 898, 7671, 554554, 767554, 45, 554155415541554, 767554, 4767]
        mk3 = [-767554554, 554767554, 17671, 0, 898, 76751, 5546554, 7677554, 47675, 554155415541554, 767554, 4767]

        #test
        self.assertTrue(bubble_sort.bubbleSort(mk1))
        self.assertTrue(bubble_sort.bubbleSort(mk2))
        self.assertTrue(bubble_sort.bubbleSort(mk3))

       

    def testLostRecords(self):
        """
        Checks that the array has not lost records
        """
        #mock
        mk1 = [767,554,1,4,554,767,554,14,45,554155415541554,767554,4]
        mk2 = [7671, 554554, 1767, 0, 898, 7671, 554554, 767554, 45, 554155415541554, 767554, 4767]
        mk3 = [7675541, 554767554, 17671, 0, 898, 76751, 5546554, 7677554, 47675, 554155415541554, 767554, 4767]

        #check that not lost records
        def CheckLost(arr1,arr2):
            return all(i in arr1 for i in arr2)

        #test
        self.assertTrue(CheckLost(bubble_sort.bubbleSort(mk1),mk1))
        self.assertTrue((CheckLost(bubble_sort.bubbleSort(mk2),mk2)))
        self.assertTrue(CheckLost(bubble_sort.bubbleSort(mk3),mk3))

  
   



    def TestSorted(arr):
        #checks if a collection is sorted
        
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))





    def testIfSorted(self):
        """
        Checking that the array is sorted
        """
        #mock
        mk1 = [767,554,-1,4,554,767,554,14,45,554155415541554,767554,4]
        mk2 = [7671, -554554, 1767, 0, 898, 7671, 554554, 767554, 45, 554155415541554, 767554, 4767]
        mk3 = [-767554554, 554767554, 17671, 0, 898, 76751, 5546554, 7677554, 47675, 554155415541554, 767554, 4767]

        #test
        self.assertTrue(BubbleSortTest.TestSorted(bubble_sort.bubbleSort(mk1)))
        self.assertTrue(BubbleSortTest.TestSorted(bubble_sort.bubbleSort(mk2)))
        self.assertTrue(BubbleSortTest.TestSorted(bubble_sort.bubbleSort(mk3)))





if __name__ == '__main__':
    unittest.main()
