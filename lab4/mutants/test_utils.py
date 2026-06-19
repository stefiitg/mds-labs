import pytest
from utils import parse_pair, unique_sorted


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_test_parse_pair__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_test_parse_pair__mutmut)
def test_parse_pair():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_orig():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_1():
    assert parse_pair(None) == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_2():
    assert parse_pair("XX1:2XX") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_3():
    assert parse_pair("1:2") != (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_4():
    assert parse_pair("1:2") == (2, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_5():
    assert parse_pair("1:2") == (1, 3)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_6():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(None):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_7():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair(None)
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_8():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("XXhelloXX")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_9():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("HELLO")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_10():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(None):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_11():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair(None)
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_12():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("XX1:2:3XX")
    with pytest.raises(ValueError):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_13():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(None):
        parse_pair("a:b")

def x_test_parse_pair__mutmut_14():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair(None)

def x_test_parse_pair__mutmut_15():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("XXa:bXX")

def x_test_parse_pair__mutmut_16():
    assert parse_pair("1:2") == (1, 2)
    with pytest.raises(ValueError):
        parse_pair("hello")
    with pytest.raises(ValueError):
        parse_pair("1:2:3")
    with pytest.raises(ValueError):
        parse_pair("A:B")

mutants_x_test_parse_pair__mutmut['_mutmut_orig'] = x_test_parse_pair__mutmut_orig # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_1'] = x_test_parse_pair__mutmut_1 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_2'] = x_test_parse_pair__mutmut_2 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_3'] = x_test_parse_pair__mutmut_3 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_4'] = x_test_parse_pair__mutmut_4 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_5'] = x_test_parse_pair__mutmut_5 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_6'] = x_test_parse_pair__mutmut_6 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_7'] = x_test_parse_pair__mutmut_7 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_8'] = x_test_parse_pair__mutmut_8 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_9'] = x_test_parse_pair__mutmut_9 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_10'] = x_test_parse_pair__mutmut_10 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_11'] = x_test_parse_pair__mutmut_11 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_12'] = x_test_parse_pair__mutmut_12 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_13'] = x_test_parse_pair__mutmut_13 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_14'] = x_test_parse_pair__mutmut_14 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_15'] = x_test_parse_pair__mutmut_15 # type: ignore # mutmut generated
mutants_x_test_parse_pair__mutmut['x_test_parse_pair__mutmut_16'] = x_test_parse_pair__mutmut_16 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_test_unique_sorted_bug__mutmut)
def test_unique_sorted_bug():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_orig():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_1():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted(None) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_2():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([2, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_3():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 3, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_4():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 4]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_5():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) != [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_6():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [2, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_7():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 3, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_8():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 4]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_9():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted(None) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_10():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([2, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_11():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 2, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_12():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 3]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_13():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) != [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_14():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [2, 2]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_15():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 3]
    assert unique_sorted([1, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_16():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted(None) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_17():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([2, 1, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_18():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 2, 1]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_19():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 2]) == [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_20():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) != [1], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_21():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [2], "Funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_22():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "XXFuncția originală va returna [1, 1] și va pica acest test!XX"

def x_test_unique_sorted_bug__mutmut_23():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "funcția originală va returna [1, 1] și va pica acest test!"

def x_test_unique_sorted_bug__mutmut_24():
    # Bug-ul ratează duplicatele dacă sunt 3 sau mai multe la rând (pentru că sare un index)
    assert unique_sorted([1, 2, 3]) == [1, 2, 3]
    assert unique_sorted([1, 1, 2]) == [1, 2]
    assert unique_sorted([1, 1, 1]) == [1], "FUNCȚIA ORIGINALĂ VA RETURNA [1, 1] ȘI VA PICA ACEST TEST!"

mutants_x_test_unique_sorted_bug__mutmut['_mutmut_orig'] = x_test_unique_sorted_bug__mutmut_orig # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_1'] = x_test_unique_sorted_bug__mutmut_1 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_2'] = x_test_unique_sorted_bug__mutmut_2 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_3'] = x_test_unique_sorted_bug__mutmut_3 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_4'] = x_test_unique_sorted_bug__mutmut_4 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_5'] = x_test_unique_sorted_bug__mutmut_5 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_6'] = x_test_unique_sorted_bug__mutmut_6 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_7'] = x_test_unique_sorted_bug__mutmut_7 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_8'] = x_test_unique_sorted_bug__mutmut_8 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_9'] = x_test_unique_sorted_bug__mutmut_9 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_10'] = x_test_unique_sorted_bug__mutmut_10 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_11'] = x_test_unique_sorted_bug__mutmut_11 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_12'] = x_test_unique_sorted_bug__mutmut_12 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_13'] = x_test_unique_sorted_bug__mutmut_13 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_14'] = x_test_unique_sorted_bug__mutmut_14 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_15'] = x_test_unique_sorted_bug__mutmut_15 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_16'] = x_test_unique_sorted_bug__mutmut_16 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_17'] = x_test_unique_sorted_bug__mutmut_17 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_18'] = x_test_unique_sorted_bug__mutmut_18 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_19'] = x_test_unique_sorted_bug__mutmut_19 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_20'] = x_test_unique_sorted_bug__mutmut_20 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_21'] = x_test_unique_sorted_bug__mutmut_21 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_22'] = x_test_unique_sorted_bug__mutmut_22 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_23'] = x_test_unique_sorted_bug__mutmut_23 # type: ignore # mutmut generated
mutants_x_test_unique_sorted_bug__mutmut['x_test_unique_sorted_bug__mutmut_24'] = x_test_unique_sorted_bug__mutmut_24 # type: ignore # mutmut generated