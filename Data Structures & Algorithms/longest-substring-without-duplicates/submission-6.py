class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        char_set = {}
        
        for i, char in enumerate(s):
            if char in char_set:
                left = max(char_set[char] + 1, left)
            char_set[char] = i
            answer = max(i - left + 1, answer)
        
        return answer