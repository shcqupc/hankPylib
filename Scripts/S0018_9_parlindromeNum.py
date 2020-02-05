print(-2**31,2**31-1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def absrev(x):
            lst = list(str(x))
            lst.reverse()
            if x==0:
                return x
            else:
                return int(''.join(lst).lstrip('0'))

        if x < -pow(2,31) or x > pow(2,31)-1:
            return 0            
        
        if x<0:
            rlst = -absrev(-x)
        else:
            rlst = absrev(x)

        if rlst < -pow(2,31) or rlst > pow(2,31)-1:
            return 0

s = Solution()
rslt = s.reverse(9646324351)
print(rslt) 

#-2147483648
#2147483647
class Solution2(object):
    def reverse(self, x):
        y , res = abs(x), 0
        if x < 0:
            boundary = 1<<31
        else:
            boundary = (1<<31)-1
        
        while(y!=0):
            res = res*10 + y%10
            y //= 10
            if res > boundary:
                return 0
        return -res if x<0 else res


s = Solution2()
rslt = s.reverse(-46324351)
print(rslt)         
