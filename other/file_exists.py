# Import the 'os' and 'unittest' modules for working with the file system and writing unit tests.
import os
import unittest

# Define a function 'file_exists' to check if a file exists in a specified directory.
def file_exists(directory, filename):
    # Create the full file path by joining the directory and filename.
    file_path = os.path.join(directory, filename)
    # Check if the file exists at the specified path.
    return os.path.exists(file_path)

# Define a test case class 'TestFileExists' that inherits from 'unittest.TestCase'.
class TestFileExists(unittest.TestCase):
    # Define a test method 'test_existing_file' to test the existence of an existing file.
    def test_existing_file(self):
        # Define the directory and filename for an existing file.
        directory = '/path/txt'
        filename = 'test1.txt'
        # Assert that the file exists in the specified directory.
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    # Define a test method 'test_nonexistent_file' to test the non-existence of a non-existing file.
    def test_nonexistent_file(self):
        # Define the directory and filename for a non-existing file.
        directory = '/path/txt'
        filename = 'test2.txt'
        # Assert that the file does not exist in the specified directory.
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()
