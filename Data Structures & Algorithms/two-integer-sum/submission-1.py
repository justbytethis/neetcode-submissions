class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            find_range = nums[i+1:]
            other = target - num
            if other in find_range:
                return [i, i + 1 + find_range.index(other)]