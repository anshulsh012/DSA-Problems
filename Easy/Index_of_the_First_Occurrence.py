haystack = "mississippi"
needle = "issip"

# Brute force:-

"""class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return -1
        
        i, j = 0, 0
        if(len(haystack) >= len(needle)):
            while(i < len(haystack)):
                for k in range(i, len(haystack)):
                    if(haystack[k] == needle[j]):
                        print(haystack[k], needle[j])
                        j+=1
                    else:
                        print(haystack[i], needle[j])
                        j = 0
                        break
                    if(j == len(needle)):
                        return i
                i+=1
        
        return -1"""

# Using KMP (Knuth-Morris-Pratt) algorithm:-

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

ans = Solution()

print(ans.strStr(haystack, needle))
