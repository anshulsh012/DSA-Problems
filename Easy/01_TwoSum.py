# Code:-

nums = [3,3]
target = 6

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp = sorted(nums[:])
        i = 0
        j = len(nums)-1
        ind = []

        while(i<j):
            ans = temp[i] + temp[j]

            if(ans<target):
                i+=1
            elif(ans>target):
                j-=1
            else:
                s = nums.index(temp[i])
                e = nums.index(temp[j])
                if(s == e):
                    for k in range(len(nums)):
                        if(temp[i] == nums[k]):
                            ind.append(k)
                    return ind
                return [s,e]

ans = Solution()

print(ans.twoSum(nums, target))