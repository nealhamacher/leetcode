class Solution(object):
    # Faster solution
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)
    
    # Less extra space used, but slower
    def isSubsequenceOld(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i = 0
        j = 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
            i += 1
        if j == len(s):
            return True
        else:
            return False
        

################################################################################

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
    s = "axc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
    s = "acb"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
    s = "abcd"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
