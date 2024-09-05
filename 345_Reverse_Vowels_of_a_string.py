#345. Reverse Vowels of a String
#Given a string s, reverse only all the vowels in the string and return #it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both #lower and upper cases, more than once.

 

#Example 1:
#Input: s = "hello"
#Output: "holle"

#Example 2:
#Input: s = "leetcode"
#Output: "leotcede"



class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) -1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i<j and s[j] not in vowels:
                j -= 1
            
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

        return ''.join(s)