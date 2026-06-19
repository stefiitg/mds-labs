

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_clamp__mutmut: MutantDict = {}  # type: ignore


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
@_mutmut_mutated(mutants_x_clamp__mutmut)
def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
mutants_x_x_clamp__mutmut_orig__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_x_clamp__mutmut_orig__mutmut)
def x_clamp__mutmut_orig(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_orig__mutmut_orig(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_orig__mutmut_1(x, lo, hi):
    if x <= lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_orig__mutmut_2(x, lo, hi):
    if x < lo:
        return lo
    if x >= hi:
        return hi
    return x

mutants_x_x_clamp__mutmut_orig__mutmut['_mutmut_orig'] = x_x_clamp__mutmut_orig__mutmut_orig # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_orig__mutmut['x_x_clamp__mutmut_orig__mutmut_1'] = x_x_clamp__mutmut_orig__mutmut_1 # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_orig__mutmut['x_x_clamp__mutmut_orig__mutmut_2'] = x_x_clamp__mutmut_orig__mutmut_2 # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_1__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_x_clamp__mutmut_1__mutmut)
def x_clamp__mutmut_1(x, lo, hi):
    if x <= lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_1__mutmut_orig(x, lo, hi):
    if x <= lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_1__mutmut_1(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
def x_x_clamp__mutmut_1__mutmut_2(x, lo, hi):
    if x <= lo:
        return lo
    if x >= hi:
        return hi
    return x

mutants_x_x_clamp__mutmut_1__mutmut['_mutmut_orig'] = x_x_clamp__mutmut_1__mutmut_orig # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_1__mutmut['x_x_clamp__mutmut_1__mutmut_1'] = x_x_clamp__mutmut_1__mutmut_1 # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_1__mutmut['x_x_clamp__mutmut_1__mutmut_2'] = x_x_clamp__mutmut_1__mutmut_2 # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_2__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_x_clamp__mutmut_2__mutmut)
def x_clamp__mutmut_2(x, lo, hi):
    if x < lo:
        return lo
    if x >= hi:
        return hi
    return x
def x_x_clamp__mutmut_2__mutmut_orig(x, lo, hi):
    if x < lo:
        return lo
    if x >= hi:
        return hi
    return x
def x_x_clamp__mutmut_2__mutmut_1(x, lo, hi):
    if x <= lo:
        return lo
    if x >= hi:
        return hi
    return x
def x_x_clamp__mutmut_2__mutmut_2(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x

mutants_x_x_clamp__mutmut_2__mutmut['_mutmut_orig'] = x_x_clamp__mutmut_2__mutmut_orig # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_2__mutmut['x_x_clamp__mutmut_2__mutmut_1'] = x_x_clamp__mutmut_2__mutmut_1 # type: ignore # mutmut generated
mutants_x_x_clamp__mutmut_2__mutmut['x_x_clamp__mutmut_2__mutmut_2'] = x_x_clamp__mutmut_2__mutmut_2 # type: ignore # mutmut generated

mutants_x_clamp__mutmut['_mutmut_orig'] = x_clamp__mutmut_orig # type: ignore # mutmut generated
mutants_x_clamp__mutmut['x_clamp__mutmut_1'] = x_clamp__mutmut_1 # type: ignore # mutmut generated
mutants_x_clamp__mutmut['x_clamp__mutmut_2'] = x_clamp__mutmut_2 # type: ignore # mutmut generated