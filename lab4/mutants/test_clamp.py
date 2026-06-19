import pytest
from hypothesis import given, assume, strategies as st
from clamp import clamp

def test_clamp_logic_branches():
    assert clamp(1, 2, 3) == 2
    assert clamp(4, 2, 3) == 3
    assert clamp(2, 1, 3) == 2
    assert clamp(2, 2, 4) == 2
    assert clamp(4, 2, 4) == 4
    assert clamp(5, 5, 5) == 5

@given(st.integers(), st.integers(), st.integers())
def test_clamp_in_bounds(x, lo, hi):
    assume(lo <= hi)
    result = clamp(x, lo, hi)
    assert lo <= result <= hi