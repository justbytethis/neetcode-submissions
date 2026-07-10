class Solution:
    def trap(self, height: List[int]) -> int:
        p, s = 0, 0
        prefix = []
        suffix = []
        for i, h in enumerate(height):
            p = max(p, h)
            prefix.append(p)
        for i, h in enumerate(reversed(height)):
            s = max(s, h)
            suffix.insert(0, s)
        
        answer = 0
        for i, h in enumerate(height):
            answer += min(prefix[i], suffix[i]) - h
        
        return answer
