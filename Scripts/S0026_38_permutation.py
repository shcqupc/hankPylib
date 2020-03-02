class Solution(object):
    def permutation(self, ss):
        """
        :type s: str
        :rtype: List[str]
        """

        def helper(s):
            if len(s) == 1:
                return s[0]
            res = []
            for i in range(len(s)):
                l = helper(s[:i] + s[i + 1:])
                for j in l:
                    res.append(s[i] + j)
            return res

        if not ss:
            return []
        words = list(set(ss))
        words.sort()
        # print(words)
        return list(sorted(set(helper(words))))

s = Solution()
print(s.permutation('aabc'))
