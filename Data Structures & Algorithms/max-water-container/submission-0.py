class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        l = len(heights)
        answer = 0
        while start < end:
            hs = heights[start]
            he = heights[end]
            answer = max(answer, min(hs, he) * (end - start))
            if (hs < he):
                start += 1
            else:
                end -= 1
        
        return answer