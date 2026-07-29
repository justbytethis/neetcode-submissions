def count_frequency(s: str) -> Dict[str, int]:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_freq = count_frequency(s1)
        start, end = 0, window_size - 1

        while end < len(s2):
            if s1_freq == count_frequency(s2[start:end+1]):
                return True
            start += 1
            end += 1

        return False