class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, ret = 0, len(nums) -1, math.inf
        if len(nums) == 1:
            return nums[0]
        while l < r:
            m = int((l+r)/2)
            ret = min(nums[m], ret)
            ret = min(nums[l], ret)
            ret = min(nums[r], ret)

            if m + 1 <= r and nums[m] > nums[m+1]:
                l = m+1
            elif m - 1 >= l and nums[m] < nums[m-1]:
                r = m-1
            else:
                l += 1
                r -= 1
            
        return ret
