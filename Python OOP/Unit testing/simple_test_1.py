import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        # arrange
        result = 'foo'.upper()
        # act
        expected_result = 'FOO'
        # assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
