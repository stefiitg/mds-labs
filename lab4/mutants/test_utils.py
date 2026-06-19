import pytest
from utils import parse_pair, unique_sorted

def test_parse_pair():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def test_unique_sorted_bug():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"