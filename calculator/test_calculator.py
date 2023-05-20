import unittest

from calculator import Calculator

class CalculatorBasicTest(unittest.TestCase):
    # AAA
    # ARRANGE |  GIVEN
    # ACT     |  WHEN
    # ASSERT  |  THEN

    def test_sum_of_two_int_numbers(self):
        # ARRANGE
        calculator = Calculator()
        first_num = 1
        second_num = 2
        expected_result = 3

        # ACT
        result = calculator.sum(first_num, second_num)

        # ASSERT
        self.assertEqual(result, expected_result)

    def test_sum_raise_typeerror_when_string_and_number_is_given(self):
        # ARRANGE
        calculator = Calculator()
        first_num = 'patata'
        second_num = 2

        with self.assertRaises(TypeError):
            calculator.sum(first_num, second_num)

    def test_sum_raise_typeerror_when_string_and_boolean_is_given(self):
        # ARRANGE
        calculator = Calculator()
        first_num = 'patata'
        second_num = True

        with self.assertRaises(TypeError):
            calculator.sum(first_num, second_num)

    def test_sum_raise_Typeerror_when_number_and_boolean_is_given(self):
        # ARRANGE
        calculator = Calculator()
        first_num = 2
        second_num = True


        with self.assertRaises(TypeError):
            calculator.sum(first_num, second_num)

    def test_sum_raise_Typeerror_when_two_strings_are_given(self):
         # ARRANGE
        calculator = Calculator()
        first_num = 'hola'
        second_num = 'Pareto'

        with self.assertRaises(TypeError):
            calculator.sum(first_num, second_num)

    def test_sum_two_natural_numbers_return_the_sum(self):
        # ARRANGE
        calculator = Calculator()
        first_num = 1.1
        second_num = 2
        expected_result = 3.1

        # ACT
        result = calculator.sum(first_num, second_num)

        # ASSERT
        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()