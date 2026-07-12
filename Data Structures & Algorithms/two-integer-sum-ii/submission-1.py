class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1,len(numbers)):
            if numbers[i-1] + numbers[i] >= target:
                compl = target - numbers[i]
                for j in range(i):
                    if numbers[j] == compl:
                        return [j+1, i+1]
