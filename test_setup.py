import unittest
from task import Fifth


class TestSetup(unittest.TestCase):

    def setUp(self):
        PLUS_TEST_SUCCESS_LIST = ["PUSH 3", "PUSH 5", "+"]
        MINUS_TEST_SUCCESS_LIST = ["PUSH 3", "PUSH 5", "-"]
        MULTIPLY_TEST_SUCCESS_LIST = ["PUSH 3", "PUSH 5", "*"]
        DIVISION_TEST_SUCCESS_LIST = ["PUSH 3", "PUSH 5", "/"]

        PLUS_TEST_FAILURE_LIST = ["PUSH 3", "PUSH 5", "POP", "+"]
        MINUS_TEST_FAILURE_LIST = ["PUSH 3", "PUSH 5", "POP", "-"]
        MULTIPLY_TEST_FAILURE_LIST = ["PUSH 3", "PUSH 5", "POP", "*"]
        DIVISION_TEST_FAILURE_LIST = ["PUSH 3", "PUSH 5", "POP", "/"]

        PUSH_TEST_SUCCESS_LIST = ["PUSH 5"]
        PUSH_TEST_FAILURE_LIST = ["PUSH X"]

        POP_TEST_SUCCESS_LIST = ["PUSH 5", "POP"]
        POP_TEST_FAILURE_LIST = ["POP"]

        SWAP_TEST_SUCCESS_LIST = ["PUSH 5", "PUSH 10", "SWAP"]
        SWAP_TEST_FAILURE_LIST = ["SWAP"]

        DUP_TEST_SUCCESS_LIST = ["PUSH 5", "DUP"]
        DUP_TEST_FAILURE_LIST = ["DUP"]

        self.fifth_plus_success = Fifth(test=True, command_list=PLUS_TEST_SUCCESS_LIST)
        self.fifth_minus_success = Fifth(test=True, command_list=MINUS_TEST_SUCCESS_LIST)
        self.fifth_multiply_success = Fifth(test=True, command_list=MULTIPLY_TEST_SUCCESS_LIST)
        self.fifth_division_success = Fifth(test=True, command_list=DIVISION_TEST_SUCCESS_LIST)

        self.fifth_plus_failure = Fifth(test=True, command_list=PLUS_TEST_FAILURE_LIST)
        self.fifth_minus_failure = Fifth(test=True, command_list=MINUS_TEST_FAILURE_LIST)
        self.fifth_multiply_failure = Fifth(test=True, command_list=MULTIPLY_TEST_FAILURE_LIST)
        self.fifth_division_failure = Fifth(test=True, command_list=DIVISION_TEST_FAILURE_LIST)

        self.fifth_push_success = Fifth(test=True, command_list=PUSH_TEST_SUCCESS_LIST)
        self.fifth_push_failure = Fifth(test=True, command_list=PUSH_TEST_FAILURE_LIST)

        self.fifth_pop_success = Fifth(test=True, command_list=POP_TEST_SUCCESS_LIST)
        self.fifth_pop_failure = Fifth(test=True, command_list=POP_TEST_FAILURE_LIST)

        self.fifth_swap_success = Fifth(test=True, command_list=SWAP_TEST_SUCCESS_LIST)
        self.fifth_swap_failure = Fifth(test=True, command_list=SWAP_TEST_FAILURE_LIST)

        self.fifth_dup_success = Fifth(test=True, command_list=DUP_TEST_SUCCESS_LIST)
        self.fifth_dup_failure = Fifth(test=True, command_list=DUP_TEST_FAILURE_LIST)

        return super(TestSetup, self).setUp()

    def tearDown(self):
        return super(TestSetup, self).tearDown()
