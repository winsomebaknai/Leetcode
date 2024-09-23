'''
1456. Maximum number of vowels in a substring of given length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowel = 0
        current_vowel = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowel += 1

        max_vowel = current_vowel

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowel += 1
            if s[i-k] in vowels:
                current_vowel -= 1
        
            max_vowel = max(max_vowel, current_vowel)
        return max_vowel

