import unittest
import extend_refactored


class Testextend_refactored(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend_refactored.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend_refactored.add(4, 1), 5)

    # to fail:
    def test_add_2_and_2_is_4(self):
        self.assertEqual(extend_refactored.add(2, 2), 4)


    def test_max_of_three_first(self):
        self.assertEqual(extend_refactored.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend_refactored.max_of_three(3, 4, 5), 5)

    # to fail: 2 is not the highest number but it is returned
    def test_max_of_three_third(self):
        self.assertEqual(extend_refactored.max_of_three(3, 3, 2), 3)


    def test_median_four(self):
        self.assertEqual(extend_refactored.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend_refactored.median([1,2,3,4,5]), 3)

    # to fail: median is not length:
    def test_median_five(self):
        self.assertEqual(extend_refactored.median([1,2,3,4,5,6]), 3.5)


    def test_is_vovel_a(self):
        self.assertTrue(extend_refactored.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend_refactored.is_vovel('u'))

    # uu was missing
    def test_is_vovel_uu(self):
        self.assertTrue(extend_refactored.is_vovel('ú'))



    def test_translate_bemutatkozik(self):
        self.assertEqual(extend_refactored.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend_refactored.translate('kolbice'), 'kovolbiviceve')

    # same vowel
    def test_translate_menni(self):
        self.assertEqual(extend_refactored.translate('menni'), 'mevennivi')

    def test_translate_megreked(self):
        self.assertEqual(extend_refactored.translate('megreked'), 'mevegrevekeved')


if __name__ == '__main__':
    unittest.main()
