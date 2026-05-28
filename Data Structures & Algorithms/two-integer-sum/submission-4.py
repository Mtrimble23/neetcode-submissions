class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            matching = target - nums[i]
            if matching in hashmap:
                return [hashmap [matching], i]
            hashmap[nums[i]] = i
        return []

            