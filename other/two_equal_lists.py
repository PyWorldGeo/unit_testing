# Import the 'unittest' module for writing unit tests.
import unittest

# Define a function 'lists_are_equal' to check if two lists are equal.
def lists_are_equal(nums1, nums2):
    return nums1 == nums2

# Define a test case class 'TestListsEquality' that inherits from 'unittest.TestCase'.
class TestListsEquality(unittest.TestCase):
    # Define a test method 'test_equal_lists' to test equal lists.
    def test_equal_lists(self):
        # Define two lists 'nums1' and 'nums2' for testing equal or unequal lists.
        nums1 = [10, 20, 30, 40]
        nums2 = [10, 20, 30, 40]
        # Uncomment one pair of 'nums1' and 'nums2' for testing equal or unequal lists.
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 50]
        print("\nEqual list test:\n", nums1, "\n", nums2)
        # Assert that the lists are equal.
        self.assertTrue(lists_are_equal(nums1, nums2), "The lists are not equal")

    # Define a test method 'test_unequal_lists' to test unequal lists.
    def test_unequal_lists(self):
        # Define two lists 'nums1' and 'nums2' for testing equal or unequal lists.
        nums1 = [10, 20, 30, 40]
        nums2 = [30, 20, 10, 40]
        # Uncomment one pair of 'nums1' and 'nums2' for testing equal or unequal lists.
        #nums1 = [10, 20, 30, 40]
        #nums2 = [10, 20, 30, 40]
        print("\nUnequal list test:\n", nums1, "\n", nums2)
        # Assert that the lists are not equal.
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are equal")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()