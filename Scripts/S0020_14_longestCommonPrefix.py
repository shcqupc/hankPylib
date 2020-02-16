class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for e in strs[1:]:
            temp = ""
            for i in range(min(len(e), len(prefix))):
                if e[i] != prefix[i]:
                    if i == 0:
                        return ""
                    break
                temp += e[i]
            prefix = temp
        return prefix


# 1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
class Solution1(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        minitem = min(strs)
        maxitem = max(strs)
        rslt = ""
        for i in range(min(len(minitem),len(maxitem))):
            if minitem[i] != maxitem[i]:
                break
            rslt += minitem[i]
        return rslt

# 2、利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
class Solution2(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        s = ""
        for i in zip(*strs):
            # print(i, set(i))
            if len(set(i)) > 1:
                break
            s += i[0]
        return s


s = Solution2()
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["aa", "a"]))
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
