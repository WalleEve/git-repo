import unittest 

class TestCase2(unittest.TestCase):
    def setUp(self):
        print("Setup method executed from testcase2 classs")

    def test_01(self):
        print("Testcase 1 executed from testcase2 class")

    def test_02(self):
        print("Testcase 2 executed from testcase2 class")

    def tearDown(self):
        print("TeadDown method executed from testcase2 class")