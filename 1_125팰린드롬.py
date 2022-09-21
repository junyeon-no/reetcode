import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
            s = re.sub('[^a-z0-9A-Z]',"",s)
            s = s.lower()
            return s == s[::-1]

class Solution2:
    def isPalindrome(self, s: str) -> bool:
            temp : str
            s = s.lower()
            s_temp = []
            for temp in s:
                if temp.isalnum() : s_temp.append(temp)
            return s_temp == s_temp[::-1]
            
sol = Solution2()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))