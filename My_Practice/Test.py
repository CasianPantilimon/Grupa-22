import unittest
import Exercitii


class TestExercitii(unittest.TestCase):
    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        test_param = 10
        result = Exercitii.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "asdasdad"
        result = Exercitii.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = Exercitii.do_stuff(test_param)
        self.assertEqual(result, "Enter a number")

    def test_do_stuff4(self):
        test_param = ""
        result = Exercitii.do_stuff(test_param)
        self.assertEqual(result, "Enter a number")

    def test_do_stuff5(self):
        test_param = 0
        result = Exercitii.do_stuff(test_param)
        self.assertEqual(result, "Enter a number")


unittest.main()
