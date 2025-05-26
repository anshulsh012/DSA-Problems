digits = [1,9,9,9]

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # set current digit to 0 and continue

        # If all digits were 9 (e.g., [9,9,9]), we now have [0,0,0]
        # Add 1 at the beginning
        return [1] + digits


ans = Solution()

print(ans.plusOne(digits))