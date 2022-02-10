
import pytest
from AnalyStockLib.simulator import simulator
import numpy as np

# class simulatorTest:

# @pytest.fixture
# def init_test():
#     param1 = 1
#     print("test start")
# @pytest.fixture(scope = "module", autouse=True)
# def assert_print():
#     simu = simulator()
#     yield simu
#     print("actual")
#     print(actual)
#     print("expected")
#     print(expected)
#     assert actual == expected

def test_moving_ave_001():
    input = [0, 0, 0, 0]
    window = 2
    simu = simulator()
    # expected = [500, 100, 10, 10]
    expected = np.array([0., 0., 0., 0.])
    actual = simu.moving_ave(input, window, False)
    print("actual")
    print(actual)
    print("expected")
    print(expected)
    assert expected.all() == actual.all()

def test_moving_ave_002():
    input = [10, 2, 10, 0]
    window = 2
    # expected = [500, 100, 10, 10]
    expected = np.array([6., 6., 5., 0.])
    simu = simulator()
    actual = simu.moving_ave(input, window, False)
    print("actual")
    print(actual)
    print("expected")
    print(expected)
    assert (expected == actual).all()

def test_rsi():
    input = [100, 100, 100, 100]
    expected = np.array([0, 0, 0, 0])
    simu = simulator()
    actual = simu.rsi(input)
    print("actual")
    print(actual)
    print("expected")
    print(expected)
    assert (expected == actual).all()

def test_rsi_002():
    input = [0, 100, 0, 100]
    expected = np.array([0, 100, 50, 50])
    simu = simulator()
    actual = simu.rsi(input)
    print("actual")
    print(actual)
    print("expected")
    print(expected)
    assert (expected == actual).all()

def test_rsi_003():
    input = [0, 100, 0, 500]
    expected = np.array([0, 100, 50, 75])
    simu = simulator()
    actual = simu.rsi(input)
    print("actual")
    print(actual)
    print("expected")
    print(expected)
    assert (expected == actual).all()