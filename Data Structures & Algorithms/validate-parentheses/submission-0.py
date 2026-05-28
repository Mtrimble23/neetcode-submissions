class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c not in my_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != my_map[c]:
                return False
            stack.pop()

        return not stack