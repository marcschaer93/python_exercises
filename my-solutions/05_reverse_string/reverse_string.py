def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse_string = phrase[::-1]
    return reverse_string


print(reverse_string('awesome'))
print(reverse_string('sauce'))
