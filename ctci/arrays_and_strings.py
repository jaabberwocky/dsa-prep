def is_unique(s: str) -> bool:
    """Implement an algorithm to determine if a string has all unique characters."""
    return len(s) == len(set(s))


def check_permutation(s1: str, s2: str) -> bool:
    """Given two strings, write a method to decide if one is a permutation of the other."""
    if len(s1) != len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)
