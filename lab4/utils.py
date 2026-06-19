def parse_pair(s):
    """Parse 'a:b' into (int, int). Raises ValueError on bad input."""
    parts = s.split(":")
    if len(parts) != 2:
        raise ValueError(f"expected 'a:b', got '{s}'")
    return int(parts[0]), int(parts[1])

def unique_sorted(lst):
    result = sorted(lst)
    i = 0
    while i < len(result) - 1:
        if result[i] == result[i + 1]:
            result.pop(i)
        else:
            i += 1  # Aici este reparația făcută de tine
    return result