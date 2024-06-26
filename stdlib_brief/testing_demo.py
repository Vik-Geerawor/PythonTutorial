import unittest
from quality_control import average


class TestQualityCheck(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)

        with self.assertRaises(ZeroDivisionError):
            average([])

        with self.assertRaises(TypeError):
            average(20, 30, 70)



if __name__ == '__main__':
    unittest.main()


# Ref: https://docs.python.org/3/tutorial/stdlib.html#quality-control
