class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        lb = {"(": ")", "[": "]", "{": "}"}
        t = []
        try:
            for l in s:
                if l in lb:
                    t.append(lb[l])
                else:
                    if l != t.pop():
                        return False
            return True if len(t) == 0 else False
        except Exception as e:
            return False
        
s = Solution()
print(s.isValid("("))
print(s.isValid("]"))
print(s.isValid(""))
print(s.isValid("()[]{}"))
print(s.isValid("{[]}"))
print(s.isValid("([)]"))
print(s.isValid("(]"))
# print(chr(40),chr(41),chr(91),chr(93),chr(123),chr(125))
