nums = [0,1,2,2,3,0,4,2]
val = 2

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        N = nums.count(val)
        for _ in range(N):
            nums.remove(val)
        
        return len(nums)
        
ans = Solution()

print(ans.removeElement(nums, val))