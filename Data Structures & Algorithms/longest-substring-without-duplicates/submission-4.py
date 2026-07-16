class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer, current = 0, 0
        char_set = {}
        for i, char in enumerate(s):
            # detect if it is the duplicated character
            # reset current/char_set if duplicated
            if char in char_set:
                char_index = char_set[char]
                current = i - char_index - 1
                char_set = {c: j for c, j in char_set.items() if j > char_index}

            # add char to char_set and increase the current length
            # update the answer
            char_set[char] = i
            current += 1
            answer = max(answer, current)
        
        return answer