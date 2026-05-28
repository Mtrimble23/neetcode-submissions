class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1;
        
        sorted_nums = sorted(num_map.keys(), key=lambda x: num_map[x], reverse=True)


        return sorted_nums[:k]