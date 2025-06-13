nums = [2,7,11,15]
target = 9

from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = {}
        
        for i, num in enumerate(nums):
            val = target - num
            
            if val in ans:
                return [ans[val], i]
            
            ans[num] = i
            
        return []

ans = Solution()

print(ans.twoSum(nums, target))