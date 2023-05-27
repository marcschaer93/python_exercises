def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = None
    letter_count = {}
    for char in phrase:
        letter_count[char] = letter_count.get(char,0) + 1
        # if char not in letter_count:
        #     letter_count[char] = 1
        # else:
        #     letter_count[char] += 1
    return letter_count 

print(multiple_letter_count("halleluja"))

