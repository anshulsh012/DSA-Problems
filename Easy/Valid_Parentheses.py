s = "}"

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            if(i in values):
                if stack:
                    top_ele = stack.pop()
                else:
                    top_ele = ""
            
                if(values[i] != top_ele):
                    return False
            else:
                stack.append(i)
        
        return not stack

ans = Solution()

print(ans.isValid(s))