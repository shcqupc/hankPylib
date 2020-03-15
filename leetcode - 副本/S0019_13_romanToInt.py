class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lst = list(s)
        num = 0
        dic2 = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C',
                '': None}  # mapping sign that may need to be reduced
        right_num = ""
        for x in range(len(lst) - 1, -1, -1):  # from right to left side
            if lst[x] == dic2[right_num]:
                num -= dic[lst[x]]
            else:
                num += dic[lst[x]]
            if lst[x] in dic2:
                right_num = lst[x]
        return num
        print(num)


class Solution2(object):
    def romanToInt(self, s) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        # return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
        # for i, n in enumerate(s):
        #     print(i, n, s[max(i - 1, 0):i + 1], d[n], d.get(s[max(i - 1, 0):i + 1], d[n]))


s = Solution2()
# s = Solution()
# s.romanToInt("III")
# s.romanToInt("IV")
# s.romanToInt("IX")
# s.romanToInt("LVIII")
rslt = s.romanToInt("MCMXCIV")
print(rslt)
