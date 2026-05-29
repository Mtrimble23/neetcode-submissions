class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        if len(nums) == 1:
            return False
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False