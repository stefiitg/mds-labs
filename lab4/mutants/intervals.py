

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_merge_intervals__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_merge_intervals__mutmut)
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_orig(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_1(intervals):
    if intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_2(intervals):
    if not intervals:
        return []
    intervals = None
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_3(intervals):
    if not intervals:
        return []
    intervals = sorted(None, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_4(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=None)
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_5(intervals):
    if not intervals:
        return []
    intervals = sorted(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_6(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, )
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_7(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: None)
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_8(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[1])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_9(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = None
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_10(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[1]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_11(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[2:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_12(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = None
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_13(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[+1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_14(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-2]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_15(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[1] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_16(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] < previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_17(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[2]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_18(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = None
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_19(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[+1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_20(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-2] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_21(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[1], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_22(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(None, current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_23(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], None))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_24(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_25(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], ))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_26(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[2], current[1]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_27(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[2]))
        else:
            merged.append(current)
    return merged
def x_merge_intervals__mutmut_28(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(None)
    return merged

mutants_x_merge_intervals__mutmut['_mutmut_orig'] = x_merge_intervals__mutmut_orig # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_1'] = x_merge_intervals__mutmut_1 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_2'] = x_merge_intervals__mutmut_2 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_3'] = x_merge_intervals__mutmut_3 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_4'] = x_merge_intervals__mutmut_4 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_5'] = x_merge_intervals__mutmut_5 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_6'] = x_merge_intervals__mutmut_6 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_7'] = x_merge_intervals__mutmut_7 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_8'] = x_merge_intervals__mutmut_8 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_9'] = x_merge_intervals__mutmut_9 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_10'] = x_merge_intervals__mutmut_10 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_11'] = x_merge_intervals__mutmut_11 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_12'] = x_merge_intervals__mutmut_12 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_13'] = x_merge_intervals__mutmut_13 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_14'] = x_merge_intervals__mutmut_14 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_15'] = x_merge_intervals__mutmut_15 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_16'] = x_merge_intervals__mutmut_16 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_17'] = x_merge_intervals__mutmut_17 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_18'] = x_merge_intervals__mutmut_18 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_19'] = x_merge_intervals__mutmut_19 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_20'] = x_merge_intervals__mutmut_20 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_21'] = x_merge_intervals__mutmut_21 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_22'] = x_merge_intervals__mutmut_22 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_23'] = x_merge_intervals__mutmut_23 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_24'] = x_merge_intervals__mutmut_24 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_25'] = x_merge_intervals__mutmut_25 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_26'] = x_merge_intervals__mutmut_26 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_27'] = x_merge_intervals__mutmut_27 # type: ignore # mutmut generated
mutants_x_merge_intervals__mutmut['x_merge_intervals__mutmut_28'] = x_merge_intervals__mutmut_28 # type: ignore # mutmut generated