class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        for num in nums:
            if num in result:
                return True
            result.append(num)
        return False