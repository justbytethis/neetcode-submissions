class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # compute frequency
        freq = {num: 0 for num in nums}
        for num in nums:
            freq[num] += 1
        
        # put it into bucket
        bucket = {i: [] for i in range(1, len(nums)+1)}
        for num in set(nums):
            bucket[freq[num]].append(num)
        
        # pick topK
        result = []
        for i in reversed(range(len(nums)+1)):
            result += bucket[i]
            if len(result) >= k:
                return result
