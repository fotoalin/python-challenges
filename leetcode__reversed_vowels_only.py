def reverse_vowels(string: str) -> str:
    """
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Constraints: 
        input string consist of printable ASCII characters
        1 <= string.length <= 3 * 105

    Example 1:
        Input: string = "hello"
        Output: "holle"

    Example 2:
        Input: string = "leetcode"
        Output: "leotcede"
    """



    def is_printable(s):
        # define a regular expression that matches non-printable characters
        non_printable_pattern = re.compile(r'[^\x20-\x7E]')
        # check if the string matches the pattern
        if non_printable_pattern.search(s):
            return False
        else:
           return True



    if len(string) < 1:
        raise ValueError('String must have at least one character')
    if len(string) > 3 * 105:
        raise ValueError('String lenght must be at most 3 * 105')
    if not is_printable(string):
        raise ValueError('The string must contains only printable characters')

      
    vowels = tuple('aeiouAEIOU')
    reversed_vowels_stack = []
    result = ''

    for char in string:
        if char in vowels:
            reversed_vowels_stack.append(char)
    
    reversed_vowels_stack.reverse()

    for char in string:
        if char in vowels:
            result += reversed_vowels_stack.pop(0) 
        else:
            result += char 

    return result



if __name__ == "__main__":
    print(reverse_vowels('Hello'))
