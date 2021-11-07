def reverse_string_string(str):

    a = ""                  # create empty string

    i = len(str)            # start at the end of string

    while i:
        i -= 1              # traverse backwards
        a += str[i]         # add substring to the string
        
    return a

def reverse_string_list(str):

    a = []                  # create empty list to hold substrings

    i = len(str)            # start at the end of string

    while i:
        i -= 1              # traverse backwards
        a.append(str[i])    # add substring to the list
        
    return ''.join(a)       # join substrings


def reverse_string_slice(str):
    return str[::-1]

# str1 = "abdab"
# a1 = "badba"

# print(reverse_string_string(str1) == a1)
# print(reverse_string_list(str1) == a1)
# print(reverse_string_slice(str1) == a1)

import timeit

str = "amanaplanacanalpanama"

print(timeit.timeit(lambda: reverse_string_string(str)))
print(timeit.timeit(lambda: reverse_string_list(str)))
print(timeit.timeit(lambda: reverse_string_slice(str)))
