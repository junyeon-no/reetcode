from typing import List, SupportsIndex

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 : return [0,1]
        nums_sort = sorted(nums)
        for i in range(0, len(nums_sort)-1):
            for j in range(i+1, len(nums_sort)):
                if nums_sort[i] + nums_sort[j] == target : 
                    rst = []
                    rst.append(nums.index(nums_sort[i]))
                    nums[rst[0]] = -1
                    rst.append(nums.index(nums_sort[j]))
                    return rst

# brute Force O(n^2)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# in 탐색 O(n^2)  ->   in 검색은 더욱 가볍고 빠르다.
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            c = target - nums[i]
            if c in nums[i+1 :] :
                return [i, nums[i+1:].index(c)+i+1]

# 해시 테이블 O(1)
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rst_dic={}
        for i, num in enumerate(nums) :
            rst_dic[num] = i

        for i, num in enumerate(nums):
            if target - num in rst_dic and i != rst_dic[target - num] : 
                return [i,rst_dic[target - num]]


    
nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
nums = [3,2,3]
tartget = 6
s = Solution4()
print(s.twoSum(nums, target))


