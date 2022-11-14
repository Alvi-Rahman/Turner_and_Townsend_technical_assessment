import unittest
from test_setup import TestSetup


class TestCalculationsSuccess(TestSetup):

    def test_plus_success(self):
        self.assertTrue(self.fifth_plus_success.run())

    def test_minus_success(self):
        self.assertTrue(self.fifth_minus_success.run())

    def test_multiply_success(self):
        self.assertTrue(self.fifth_multiply_success.run())

    def test_division_success(self):
        self.assertTrue(self.fifth_division_success.run())


class TestCalculationsFailure(TestSetup):

    def test_plus_failure(self):
        self.assertFalse(self.fifth_plus_failure.run())

    def test_minus_failure(self):
        self.assertFalse(self.fifth_minus_failure.run())

    def test_multiply_failure(self):
        self.assertFalse(self.fifth_multiply_failure.run())

    def test_division_failure(self):
        self.assertFalse(self.fifth_division_failure.run())


class TestOperationSuccess(TestSetup):

    def test_push_success(self):
        self.assertTrue(self.fifth_push_success.run())

    def test_pop_success(self):
        self.assertTrue(self.fifth_pop_success.run())

    def test_swap_success(self):
        self.assertTrue(self.fifth_swap_success.run())

    def test_dup_success(self):
        self.assertTrue(self.fifth_dup_success.run())


class TestOperationFailure(TestSetup):

    def test_push_success(self):
        self.assertFalse(self.fifth_push_failure.run())

    def test_pop_success(self):
        self.assertFalse(self.fifth_pop_failure.run())

    def test_swap_success(self):
        self.assertFalse(self.fifth_swap_failure.run())

    def test_dup_success(self):
        self.assertFalse(self.fifth_dup_failure.run())


if __name__ == '__main__':
    unittest.main()
