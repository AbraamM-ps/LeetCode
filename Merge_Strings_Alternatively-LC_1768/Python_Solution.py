class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        combinedWord = []
        length = max(len(word1), len(word2))
        for i in range(length):
            if (i < len(word1)):
                combinedWord.append(word1[i])
            if (i < len(word2)):
                combinedWord.append(word2[i])
        return ''.join(combinedWord)

        # Space Complexity O(T)
        # Time Complexity O(T)
