"""
A module for testing the simple interest calculator function.

Module contents:
  - Tests for standard simple interest calculations.
  - Tests for edge cases where inputs such as principal, rate, or time are zero.
  - Validation of correct implementation based on the simple interest formula.
"""

import sys
import os
import unittest

# Add the project root directory to sys.path
project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.append(project_root)

# Debug: Print sys.path to verify
print("sys.path:", sys.path)

from ..simple_interest_calculator import calculate_simple_interest


class TestSimpleInterestCalculator(unittest.TestCase):
    """Unit tests for the Simple Interest Calculator."""

    def test_calculate_simple_interest(self):
        """It should return 150 when the principal is 1000, rate is 5%, and time is 3 years."""
        principal = 1000
        rate_of_interest = 5
        time = 3

        expected_result = 150
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_principal(self):
        """It should return 0 when the principal is 0."""
        principal = 0
        rate_of_interest = 5
        time = 3

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_time(self):
        """It should return 0 when the time is 0."""
        principal = 1000
        rate_of_interest = 5
        time = 0

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_rate(self):
        """It should return 0 when the rate of interest is 0."""
        principal = 1000
        rate_of_interest = 0
        time = 3

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
