s = "MCMXCIV"

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for j in range(len(s)):
            if(j < len(s)-1 and values[s[j]] < values[s[j+1]]):
                ans-=values[s[j]]
            elif(s[j] in values):
                ans+=values[s[j]]
        return ans
    
ans = Solution()

print(ans.romanToInt(s))