VOWELS = set("aeiou")

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # count = {}
    # phrase = phrase.lower()

    # for char in phrase:
    #     if char in 'aeiou':
    #         if char in count.keys():
    #             count[char] += 1
    #         else:
    #             count[char] = 1

    # return count


    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter