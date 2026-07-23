class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0

        # Left to right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left
        left = 0
        right = 0

        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0

        return max_length
