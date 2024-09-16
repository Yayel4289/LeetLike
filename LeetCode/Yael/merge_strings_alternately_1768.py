class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        res = ""
        for i in range(len(max(word1, word2, key=len))):
            res += word1[i] if i < len(word1) else " "
            res += word2[i] if i < len(word2) else " "
        return res.replace(" ", "")



