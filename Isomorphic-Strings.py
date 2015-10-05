class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        compareDict = {}
        for index, val in enumerate(s):
            if s[index] in compareDict.keys():
                if compareDict[s[index]] != t[index]:
                    return False
            elif t[index] in compareDict.values():
                    return False
            else:
                compareDict[s[index]] = t[index]
        return True


