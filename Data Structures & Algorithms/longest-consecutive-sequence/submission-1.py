class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_before = [(num-1 in nums_set) for num in nums]
        max_length = 0

        for i, num in enumerate(nums):
            length = 1
            if not nums_before[i]:
                current_num = num
                while True:
                    if current_num+1 in nums_set:
                        current_num += 1
                        length += 1
                    else:
                        break
            
            max_length = max(max_length, length)
        
        return max_length