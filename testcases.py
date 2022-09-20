import unittest
import solution

class Testsolution(unittest.TestCase):
    def test_second_max(self):
        num_inputs = 3
        test_cases = ['1 2 3','10 15 5','100 999 500']
        result = solution.second_max(num_inputs,test_cases)
        self.assertEqual(result,'2\n10\n500')
        print(f"Output:\n{result}")

    def test_sum_digits_in_string(self):
        num_inputs = 1
        test_cases = ['ab1231da']
        result = solution.sum_digits_in_string(num_inputs,test_cases)
        self.assertEqual(result,'7')
        print(f"Output:\n{result}")


if __name__ == '__main__':
    unittest.main()