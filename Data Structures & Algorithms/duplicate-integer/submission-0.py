class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index, item in enumerate(nums):
            if index >= len(nums) -1:
                break
            if item == nums[index + 1]:
                return True
        return False
