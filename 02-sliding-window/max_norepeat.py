# Given a string, find the length of the longest substring(s) that is not repeating.

def max_norepeat(string):
    a = 0
    
    if list(string):
        start = 0 # starting pointer
        seen = {} # creates hash map of unique characters

        for i, char in enumerate(string):

            if char in seen and start <= seen[char]:
                start = seen[char] + 1

            else:
                a = max(a, i - start + 1)

            seen[char] = i

    return a

s1 = "abcda"
a1 = 4
# ["abcd", "bcda"]
print(max_norepeat(s1) == a1)

s2 = "aabcdefaadcgg"
a2 = 6
# ["abcdef"]
print(max_norepeat(s2) == a2)

s3 = ""
a3 = 0
print(max_norepeat(s3) == a3)
