strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = strs[0]
        
        for val in strs[1:]:
            res = ""
            for i in range(min(len(ans), len(val))):
                if(ans[i] == val[i]):
                    res = res+ans[i]
                else:
                    break
            ans = res    
        return ans

ans = Solution()

print(ans.longestCommonPrefix(strs))