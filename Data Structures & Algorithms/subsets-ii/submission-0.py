class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(curr, i):
            if i == len(nums):
                res.add(tuple(curr))
                return
            
            backtrack(curr, i + 1)

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
        nums.sort()
        backtrack([], 0)
        return [list(s) for s in res]