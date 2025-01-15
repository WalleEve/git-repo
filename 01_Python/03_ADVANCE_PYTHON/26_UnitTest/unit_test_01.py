import unittest


class SampleTest(unittest.TestCase):

    def setUp(self):
        print("setUp method execution.")

    def test_01(self):
        print("test method execution..")

    def tearDown(self):
        print("tearDown method execution..")


unittest.main()