from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        rst : int = 0
        nums.sort()
        while len(nums) != 0 :
            n1 = nums.pop()
            n2 = nums.pop()
            if n1 > n2 : rst+=n2
            else : rst+=n1
        return rst



nums = [1,4,3,2]
# nums = [6,2,6,5,1,2]
s = Solution()
print(s.arrayPairSum(nums))