import pytest
# from yatzi_engine import full_house
from src.yatzi_engine import full_house


def test_full_house():
    assert full_house([1,1,2,2,2]) == 8
    # assert full_house([5,5,6,6,6]) == 28