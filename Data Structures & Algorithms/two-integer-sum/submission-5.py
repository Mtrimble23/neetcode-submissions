class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            search = target - nums[i]
            if search in num_map:
                return [num_map[search], i]
            num_map[nums[i]] = i

        return []

