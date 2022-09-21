class Solution:
    def reverseString(self, s:list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print(s)

sol = Solution()
s = ["h","e","l","l","o"]
sol.reverseString(s)