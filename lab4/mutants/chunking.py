

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_chunk__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_chunk__mutmut)
def chunk(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
def x_chunk__mutmut_orig(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
def x_chunk__mutmut_1(lst, n):
    return [lst[i:i - n] for i in range(0, len(lst), n)]
def x_chunk__mutmut_2(lst, n):
    return [lst[i:i + n] for i in range(None, len(lst), n)]
def x_chunk__mutmut_3(lst, n):
    return [lst[i:i + n] for i in range(0, None, n)]
def x_chunk__mutmut_4(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), None)]
def x_chunk__mutmut_5(lst, n):
    return [lst[i:i + n] for i in range(len(lst), n)]
def x_chunk__mutmut_6(lst, n):
    return [lst[i:i + n] for i in range(0, n)]
def x_chunk__mutmut_7(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), )]
def x_chunk__mutmut_8(lst, n):
    return [lst[i:i + n] for i in range(1, len(lst), n)]

mutants_x_chunk__mutmut['_mutmut_orig'] = x_chunk__mutmut_orig # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_1'] = x_chunk__mutmut_1 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_2'] = x_chunk__mutmut_2 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_3'] = x_chunk__mutmut_3 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_4'] = x_chunk__mutmut_4 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_5'] = x_chunk__mutmut_5 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_6'] = x_chunk__mutmut_6 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_7'] = x_chunk__mutmut_7 # type: ignore # mutmut generated
mutants_x_chunk__mutmut['x_chunk__mutmut_8'] = x_chunk__mutmut_8 # type: ignore # mutmut generated

def flatten(lst_of_lsts):
    return [item for sublist in lst_of_lsts for item in sublist]