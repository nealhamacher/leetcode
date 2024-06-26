class Solution(object):
    # Runtime - 16 ms, beats 97.47%, Memory - 11.51MB, beats 83.49%
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sum = 0
        while i < len(s):
            if s[i] == 'M':
                sum += 1000
            elif s[i] == 'D':
                sum += 500
            elif s[i] == 'C': 
                if (i < len(s) - 1) and (s[i+1] == 'M' or s[i+1] == 'D'):
                    sum -= 100
                else:
                    sum += 100
            elif s[i] == 'L':
                sum += 50
            elif s[i] == 'X':
                if (i < len(s) - 1) and (s[i+1] == 'C' or s[i+1] == 'L'):
                    sum -= 10
                else:
                    sum += 10
            elif s[i] == 'V':
                sum += 5
            elif s[i] == 'I':
                if (i < len(s) - 1) and (s[i+1] == 'X' or s[i+1] == 'V'):
                    sum -= 1
                else:
                    sum += 1
            i += 1
        return sum

    # While loops and works in reverse, not significant change in performance
    # Runtime - 23 ms, beats 86.02%. Memory - 11.68MB, beats 52.15%
    def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        sum = 0
        while s[i] == "I":
            sum += 1
            i -= 1
            if i < 0:
                return sum
        while s[i] == "V":
            sum += 5
            i -= 1
            if i < 0:
                return sum
        while s[i] == "I":
            sum -= 1
            i -= 1
            if i < 0:
                return sum
        while s[i] == "V":
            sum += 5
            i -= 1
            if i < 0:
                return sum
        while s[i] == "X":
            sum += 10
            i -= 1
            if i < 0:
                return sum
        while s[i] == "I":
            sum -= 1
            i -= 1
            if i < 0:
                return sum
        while s[i] == "X":
            sum += 10
            i -= 1
            if i < 0:
                return sum
        while s[i] == "L":
            sum += 50
            i -= 1
            if i < 0:
                return sum
        while s[i] == "X":
            sum -= 10
            i -= 1
            if i < 0:
                return sum
        while s[i] == "L":
            sum += 50
            i -= 1
            if i < 0:
                return sum
        while s[i] == "C":
            sum += 100
            i -= 1
            if i < 0:
                return sum
        while s[i] == "X":
            sum -= 10
            i -= 1
            if i < 0:
                return sum
        while s[i] == "C":
            sum += 100
            i -= 1
            if i < 0:
                return sum
        while s[i] == "D":
            sum += 500
            i -= 1
            if i < 0:
                return sum
        while s[i] == "C":
            sum -= 100
            i -= 1
            if i < 0:
                return sum
        while s[i] == "D":
            sum += 500
            i -= 1
            if i < 0:
                return sum
        while s[i] == "M":
            sum += 1000
            i -= 1
            if i < 0:
                return sum
        while s[i] == "C":
            sum -= 100
            i -= 1
            if i < 0:
                return sum
        while s[i] == "M":
            sum += 1000
            i -= 1
            if i < 0:
                return sum
        return sum

    # Runtime - 34 ms, beats 36.96%, Memory - 11.63MB, beats 52.60%
    def romanToIntOLD(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sum = 0
        while i < len(s):
            if s[i] == 'M':
                sum += 1000
            if s[i] == 'D':
                sum += 500
            if s[i] == 'C': 
                if (i < len(s) - 1) and (s[i+1] == 'M' or s[i+1] == 'D'):
                    sum -= 100
                else:
                    sum += 100
            if s[i] == 'L':
                sum += 50
            if s[i] == 'X':
                if (i < len(s) - 1) and (s[i+1] == 'C' or s[i+1] == 'L'):
                    sum -= 10
                else:
                    sum += 10
            if s[i] == 'V':
                sum += 5
            if s[i] == 'I':
                if (i < len(s) - 1) and (s[i+1] == 'X' or s[i+1] == 'V'):
                    sum -= 1
                else:
                    sum += 1
            i += 1
        return sum


################################################################################

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToIntOLD("III"))
    print(sol.romanToIntOLD("LVIII"))
    print(sol.romanToIntOLD("MCMXCIV"))

    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))

    print(sol.romanToInt2("III"))
    print(sol.romanToInt2("LVIII"))
    print(sol.romanToInt2("MCMXCIV"))