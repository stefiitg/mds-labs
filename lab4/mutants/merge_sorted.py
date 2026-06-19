

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_merge_sorted__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_merge_sorted__mutmut)
def merge_sorted(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_orig(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_1(a, b):
    result = None
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_2(a, b):
    result = []
    i, j = None
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_3(a, b):
    result = []
    i, j = 1, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_4(a, b):
    result = []
    i, j = 0, 1
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_5(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_6(a, b):
    result = []
    i, j = 0, 0
    while i <= len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_7(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j <= len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_8(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_9(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(None)
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_10(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i = 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_11(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i -= 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_12(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 2
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_13(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(None)
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_14(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j = 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_15(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j -= 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_16(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 2
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_17(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(None)
    result.extend(b[j:])
    return result
def x_merge_sorted__mutmut_18(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(None)
    return result

mutants_x_merge_sorted__mutmut['_mutmut_orig'] = x_merge_sorted__mutmut_orig # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_1'] = x_merge_sorted__mutmut_1 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_2'] = x_merge_sorted__mutmut_2 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_3'] = x_merge_sorted__mutmut_3 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_4'] = x_merge_sorted__mutmut_4 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_5'] = x_merge_sorted__mutmut_5 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_6'] = x_merge_sorted__mutmut_6 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_7'] = x_merge_sorted__mutmut_7 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_8'] = x_merge_sorted__mutmut_8 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_9'] = x_merge_sorted__mutmut_9 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_10'] = x_merge_sorted__mutmut_10 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_11'] = x_merge_sorted__mutmut_11 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_12'] = x_merge_sorted__mutmut_12 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_13'] = x_merge_sorted__mutmut_13 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_14'] = x_merge_sorted__mutmut_14 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_15'] = x_merge_sorted__mutmut_15 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_16'] = x_merge_sorted__mutmut_16 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_17'] = x_merge_sorted__mutmut_17 # type: ignore # mutmut generated
mutants_x_merge_sorted__mutmut['x_merge_sorted__mutmut_18'] = x_merge_sorted__mutmut_18 # type: ignore # mutmut generated