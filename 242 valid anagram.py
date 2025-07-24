#https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        #Every char in string s has now been map to hash map
        #with value how many times it appeared.
        #get(key, value)

        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            #loop over t and checks if the char is in dictionary
            #if yes decrement

        for i in count.values():
            if i != 0:
                return False
        #if its a perfect match of all characters the count should be zero
        #if its zero return true else false
        return True
