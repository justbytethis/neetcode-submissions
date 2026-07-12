class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        non_zero_product = 1
        zero_count = 0
        result = []
        for num in nums:
            if not num == 0:
                all_product *= num
            else:
                zero_count += 1
        
        if zero_count >= 2:
            return [0 for num in nums]
        elif zero_count == 1:
            return [all_product if num == 0 else 0 for num in nums]
        else:
            return [all_product // num for num in nums]