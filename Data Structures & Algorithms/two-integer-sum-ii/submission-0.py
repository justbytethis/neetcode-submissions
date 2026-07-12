class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_set = set(numbers)
        for i, num in enumerate(numbers):
            if target - num in numbers_set:
                for j, comp in enumerate(numbers):
                    if comp == target - num and i != j:
                        return [i+1, j+1]