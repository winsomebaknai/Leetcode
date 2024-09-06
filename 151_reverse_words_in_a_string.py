#151. Reverse words in a string
#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s #will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single #space.

#Note that s may contain leading or trailing spaces or multiple spaces #between two words. The returned string should only have a single space #separating the words. Do not include any extra spaces.

#Example 1:

#Input: s = "the sky is blue"
#Output: "blue is sky the"




class Solution:
    def reverseWords(self, s: str) -> str:
        #doing it without the in build functions
        start = 0
        end  = len(s) -1

        while start <= end and s[start] == ' ':
            start += 1

        while end >= start and s[end] == ' ':
            end -= 1

        #split the strings to words
        words = []
        word = []
        while start <= end:
            if s[start] != " ":
                word.append(s[start])
            elif word:
                words.append("".join(word))
                word = []
            start += 1
        
        if word:
            words.append("".join(word))
        
        #Reverse the words list
        reverse_words = []
        for i in range(len(words)-1, -1, -1):
            reverse_words.append(words[i])
        
        #join the words with single space
        result = ''
        for i in range(len(reverse_words)):
            result += reverse_words[i]
            if i != len(reverse_words) - 1:
                result += ' '
    
        return result



