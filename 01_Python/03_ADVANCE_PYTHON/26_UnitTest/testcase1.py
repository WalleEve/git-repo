import unittest 

class TestCase1(unittest.TestCase):
    def setUp(self) -> None:
        print("Setup Methods Executed from testcase1 class")

    def test_01(self):
        print("Testcase 1 executed from testcase1 class")

    def test_02(self):
        print("Testcase 2 executed from testcase1 class")

    def tearDown(self) -> None:
        print("Teardown method executed from testcase1 class")

