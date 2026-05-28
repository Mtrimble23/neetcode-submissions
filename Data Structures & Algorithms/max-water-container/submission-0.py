class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = -math.inf
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            ret = max(ret, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return ret