class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            fac=1
            while(x //fac >=10):
                fac *=10
            while(x>0):
                left = x//fac
                right = x %10
                x = x%fac//10
                fac /=100
                print(left,right,x,fac)
                if left != right:
                    return False         
        return True

s = Solution()
rslt = s.isPalindrome(1)
print(rslt)         


class Solution2(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:        
            rev = 0 
            while(x > rev):
                rev = rev*10 + x % 10
                if rev == 0:
                    return False
                x //=10
        print(rev,x)
        if x == rev or x == rev //10:
            return True
        return False
    
s = Solution2()
rslt = s.isPalindrome(10)
print(rslt)      
