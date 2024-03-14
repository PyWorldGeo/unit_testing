#Write a Python unit test program to check if a given number is prime or not.


# Import the 'unittest' module for writing unit tests.
import unittest

# Define a function 'is_prime' to check if a number is prime.
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.TestCase'.
class PrimeNumberTestCase(unittest.TestCase):
    # Define a test method 'test_prime_numbers' to test prime numbers.
    def test_isPrime(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        # You can use the alternative 'prime_numbers' list by uncommenting it.
        # prime_numbers = [2, 3, 4, 8, 11, 13, 17, 19, 23, 30, 31]
        print("Prime numbers:", prime_numbers)
        # Iterate through prime numbers and assert that they are recognized as prime.
        for number in prime_numbers:
            self.assertTrue(isPrime(number), f"{number} is not recognized as a prime number")


        non_prime_numbers = [4, 6, 2, 10, 12, 14, 16, 18, 20]
        # You can use the alternative 'non_prime_numbers' list by uncommenting it.
        # non_prime_numbers = [4, 6, 8, 9, 11, 12, 14, 17, 16, 18, 20]
        print("Non-prime numbers:", non_prime_numbers)
        # Iterate through non-prime numbers and assert that they are not recognized as prime.
        for number in non_prime_numbers:
            self.assertFalse(isPrime(number), f"{number} is incorrectly recognized as a prime number")

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()


#python prime_or_not.py PrimeNumberTestCase.test_prime