from unittest import TestCase
from countpigs import CountPigs, directcountpigs, expect_val, f, p


class TestSimulation(TestCase):
    def test_direct_count_cls(self):
        c = CountPigs(5)
        # (n, q, m, k) = (5, 1, 3, 2)
        choice = c.choice(1)
        choices = c.choices(1, 3)
        choose = c.choose(1, 3, 2)
        self.assertEqual(len(choice), 5)
        self.assertEqual(len(choices), 125)
        self.assertEqual(len(choose), 60)
        # (n, q, m, k) = (5, 2, 3, 3)
        choice = c.choice(2)
        choices = c.choices(2, 3)
        choose = c.choose(2, 3, 3)
        self.assertEqual(len(choice), 10)
        self.assertEqual(len(choices), 1000)
        self.assertEqual(len(choose), 240)

    def test_direct_count_func(self):
        # (n, q, m, k) = (5, 1, 3, 2)
        x0, x1 = directcountpigs(5, 1, 3, 2)
        self.assertEqual(x0, 125)
        self.assertEqual(x1, 60)
        # (n, q, m, k) = (5, 2, 3, 3)
        x0, x1 = directcountpigs(5, 2, 3, 3)
        self.assertEqual(x0, 1000)
        self.assertEqual(x1, 240)


class TestRecursion(TestCase):
    def test_counting_factor(self):
        self.assertEqual(f(5, 1, 3), 150)
        self.assertEqual(f(5, 2, 3), 240)
        self.assertEqual(f(10, 3, 7), 2687077316815500)

    def test_probability(self):
        self.assertEqual(p(5, 3, 1, 2), 12/25)
        self.assertEqual(p(5, 3, 2, 3), 6/25)
        self.assertEqual(p(4, 3, 1, 1) + p(4, 3, 1, 2) + p(4, 3, 1, 3), 1)

    def test_expectation(self):
        self.assertEqual(expect_val(4, 3, 1), 37/16)
        self.assertEqual(expect_val(10, 5, 3), 83193/10000)
        # self.assertEqual(expect_val(15, 7, 3), 185223/15625)  fail
        self.assertAlmostEqual(expect_val(15, 7, 3), 185223/15625)
        self.assertEqual(expect_val(20, 10, 3), 8224006099551/512000000000)
