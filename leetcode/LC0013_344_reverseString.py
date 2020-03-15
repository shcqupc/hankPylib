class Solution(object):
    # regression
    def reverseString1(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        def helper(start_idx, end_idx, s):
            if start_idx < end_idx:
                s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
                s = helper(start_idx + 1, end_idx - 1, s)
            return s

        return helper(0, len(s) - 1, s)

    # loop
    def reverseString2(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


s = Solution()
print(s.reverseString2([5, 4, 3, 2, 1]))
