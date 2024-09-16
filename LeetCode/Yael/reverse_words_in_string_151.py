class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        tmp = ""
        for letter in s + " ":
            if letter != " ":
                tmp += letter
            elif tmp != "":
                res = tmp + (" " if res != "" else "") + res
                tmp = ""
        return res
