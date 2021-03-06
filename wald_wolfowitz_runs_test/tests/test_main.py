from nose.tools import assert_equal, assert_almost_equal, assert_greater, assert_less_equal, assert_true, assert_false
from runs_test import _calculate_nruns, _calculate_p_value, _calculate_mean
from wald_wolfowitz_runs_test.runs_test import *
import numpy as np

"""
High level testing of the package.
"""


class TestMain(object):
    def test_calculate_p_value(self):
        p_val34 = _calculate_p_value(-3.4)
        assert_almost_equal((1-.9996), p_val34, delta=0.0001)
        p_val09 = _calculate_p_value(-0.9)
        assert_almost_equal(.1841, p_val09, delta=0.0001)
        p_val1 = _calculate_p_value(-1)
        assert_almost_equal(.15865, p_val1, delta=0.0001)

    def test_runs_chisquare(self):
        list_dist_A = np.random.chisquare(1, 1000)
        list_dist_B = np.random.exponential(4, 1000)
        assert_true(runs(list_dist_A, list_dist_B)[0])

        list_dist_A = np.random.chisquare(1, 1000)
        list_dist_B = np.random.chisquare(1, 1000)
        p_val = runs(list_dist_A, list_dist_B)[1]
        p_val2 = runs(list_dist_B, list_dist_A)[1]
        assert_equal(p_val, p_val2)
        assert_false(runs(list_dist_A, list_dist_B)[0])

    def test_runs_exponential(self):
        list_dist_A = np.random.exponential(2, 1000)
        list_dist_B = np.random.chisquare(5, 1000)
        assert_true(runs(list_dist_A, list_dist_B)[0])

        list_dist_A = np.random.exponential(1, 2000)
        list_dist_B = np.random.exponential(1, 2000)
        assert_false(runs(list_dist_A, list_dist_B)[0])

    def test_calculate_nruns(self):
        constant_list = ["A"] * 100
        assert_equal(1, _calculate_nruns(constant_list))
        rising_list = range(0, 1000)
        assert_equal(1000, _calculate_nruns(rising_list))
        binary_list = ["X"] * 5 + ["y"] * 5 + ["X"] * 5
        assert_equal(3, _calculate_nruns(binary_list))

    def test_calculate_mean(self):
        """
        This is simple arithmetics 
        :return: void
        """
        assert_equal(6, _calculate_mean(5, 5))
