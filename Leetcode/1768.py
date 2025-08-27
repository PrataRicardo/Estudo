class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''

        if len(word1) > len(word2): 
            smallW = word2
            bigW = word1
        else: 
            smallW = word1
            bigW = word2

        if word1 == smallW:
            for i in range(len(smallW)):
                output +=  word1[i] + word2[i]
            for j in range(len(smallW), len(bigW)):
                output +=  word2[j]
        if word2 == smallW:
            for i in range(len(smallW)):
                output += word1[i] + word2[i]
            for j in range(len(smallW), len(bigW)):
                output += word1[j]

        return output