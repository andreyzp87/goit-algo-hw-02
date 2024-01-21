import re
from collections import deque


def is_palindrome(s):
    s = s.lower()
    s = re.sub("[^0-9a-zA-Z]+", "", s)
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    palindromes = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Able was I ere I saw Elba",
        "No 'x' in 'Nixon'",
        "Was it a Rat I saw?",
    ]

    for palindrome in palindromes:
        print('"' + palindrome + '"', is_palindrome(palindrome))
