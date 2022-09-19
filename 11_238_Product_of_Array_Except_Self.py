from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rst = []
        p = 1
        #왼쪽 곱셈
        for i in range(0, len(nums)):
            rst.append(p)
            p = p*nums[i]
        p=1
        #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) -1, 0-1, -1):
            rst[i] = rst[i] * p
            p = p * nums[i]
        return rst

nums =  [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))