# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    w = ''.join(sorted(word))
    a = ''.join(sorted(anagram))
    if(w == a):
        return True
    else:
        return False
find_anagram('Fear','Fare')
# result = find_anagram('Fear','Fare')
# print(result)
