def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWEL = 'aeiou'
    letters = {}
    # for char in phrase.lower():
    #     if char in VOWEL:
    #         if char not in letters:
    #             letters[char] = 1
    #         else:
    #             letters[char] += 1 
    # return letters     

    for char in phrase.lower():
        if char in VOWEL:
            letters[char] = letters.get(char, 0) + 1
    return letters    

#The `get` method takes two arguments: the first argument is the key to look up in the dictionary, and the second argument is the default value to return if the key is not present in the dictionary.
#In this case, the `get` method is called with the key `char` and a default value of `0`. If the character `char` is already in the `letters` dictionary, the `get` method will return its current count as an integer. If `char` is not in the dictionary, it will return the default value of `0`.
#The line of code then increments this count by 1:

# Here's a JavaScript implementation of the `vowel_count` function:

# ```
# function vowelCount(phrase) {
#   const VOWELS = "aeiou";
#   const letters = {};

#   for (let char of phrase.toLowerCase()) {
#     if (VOWELS.includes(char)) {
#       letters[char] = letters[char] + 1 || 1;
#     }
#   }

#   return letters;
# }

# console.log(vowelCount("rithm school")); // {i: 1, o: 2}
# console.log(vowelCount("HOW ARE YOU? i am great!")); // {o: 2, a: 3, e: 2, u: 1, i: 1}

# ```

# In this implementation, a `const` variable `VOWELS` is declared with the vowels that we're interested in counting. Then, an empty object `letters` is declared to store the counts of each vowel.

# A `for...of` loop is used to iterate over each character in the `phrase`. The `toLowerCase()` method is called on each character to make it lowercase, so that we can compare it to the lowercase vowels in `VOWELS`. The `includes()` method is used to check if the current character is a vowel.

# If the current character is a vowel, we use the `||` operator to determine whether `letters[char]` already exists. If it does, we increment its value by `1`. If it doesn't, we set its value to `1`.

# Finally, we return the `letters` object with the counts of each vowel.

# I hope that helps! Let me know if you have any further questions or if there's anything else I can assist you with.


    
