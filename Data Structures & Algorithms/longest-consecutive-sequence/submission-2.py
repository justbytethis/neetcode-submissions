class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for i, num in enumerate(nums):
            length = 1
            if not (num-1 in nums_set):
                while num + length in nums_set:
                    length += 1
            
            max_length = max(max_length, length)
        
        return max_length