class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while True:
            number_sum = numbers[i] + numbers[j]
            if number_sum == target:
                return [i+1, j+1]
            elif number_sum > target:
                j -= 1
            else:
                i += 1