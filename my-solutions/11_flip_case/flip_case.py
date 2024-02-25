def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # swapped_phrase = []
    # for letter in phrase:
    #     if letter == to_swap:
    #         if letter == letter.upper():
    #             swapped_phrase.append(letter.lower())
    #         elif letter == letter.lower():
    #             swapped_phrase.append(letter.upper())
    #     else: 
    #             swapped_phrase.append(letter)

    # return ''.join(swapped_phrase)

    swapped_phrase = []
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            swapped_phrase.append(letter.swapcase())
        else:
            swapped_phrase.append(letter)
    return "".join(swapped_phrase)

