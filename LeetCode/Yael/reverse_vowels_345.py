class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = "aeiouAEIOU"
        length = len(s)
        left_res = ""
        right_res = ""
        i = 0
        j = length - 1
        while i < j:
            if s[i] in vowels:
                if s[j] in vowels:
                    left_res += s[j]
                    right_res = s[i] + right_res
                    i += 1
                    j -= 1
                    continue
                right_res = s[j] + right_res
                j -= 1
                continue
            left_res += s[i]
            i += 1
        if i == j:
            left_res += s[i]
        return left_res + right_res
