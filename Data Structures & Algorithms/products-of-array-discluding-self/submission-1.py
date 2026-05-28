class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            new_add = 1

            for j in range(len(nums)):
                if(i != j):
                    new_add = new_add * nums[j]
            result.append(new_add)
        
        return result