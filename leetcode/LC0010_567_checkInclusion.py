'''给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic = {}
        dic_window = {}
        for chr in s1:
            dic.setdefault(chr, 0)
            dic[chr] = dic[chr] + 1

        window = ""
        for x in s2:
            if x in dic:
                dic_window.setdefault(x, 0)
                dic_window[x] = dic_window[x] + 1
                # print(dic_window,dic)
                if dic_window == dic:  # find substring
                    return True
                else:  # lack of other char OR char number exceed
                    window += x  # right cursor move forward
                    if dic_window[x] > dic[x]:  # char number exceed
                        # left cursor move forward to second x
                        window = window[window.find(x) + 1:]
                        dic_window.clear()
                        for w in window:
                            dic_window.setdefault(w, 0)
                            dic_window[w] = dic_window[w] + 1
                        # print(window, dic_window)
            else:
                dic_window.clear()
                window = ""
        return False


s = Solution()
print(s.checkInclusion('aab', '()**&babaee'))
print(s.checkInclusion('ab', 'eidbaooo'))
print(s.checkInclusion('ab', 'eidboaoo'))
