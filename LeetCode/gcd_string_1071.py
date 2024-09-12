class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            self.gcdOfStrings(str2, str1)

        if not len(str2):
            return str1

        div = False
        while str1[-len(str2):] == str2:
            div = True
            str1 = str1[:-len(str2)]

        if not div:
            return ""

        return self.gcdOfStrings(str2, str1)


a = Solution()
print(a.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
