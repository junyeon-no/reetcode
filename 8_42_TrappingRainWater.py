from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        self.right = 0
        self.left = 0
        self.volume = 0
        # max 찾기
        self.max = max(height)
        
        #왼쪽 부터 max까지 volume 구하기
        for i in range(0,height.index(self.max)):
            if(height[i] > self.left):self.left = height[i]
            else : self.volume += self.left - height[i]

        #오른 쪽부터 max까지 volume 구하기
        for num in height[height.index(self.max):][::-1]:
            if self.right < num : self.right = num
            else : self.volume += self.right-num
        return self.volume
            
class Solution2:
    def trap(self, height: List[int]) -> int:
        self.volume = 0
        
        return self.volume
        


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
height = [4,2,0,3,2,5,0,5,2,4]
s = Solution()
print(s.trap(height))

