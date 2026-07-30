class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        
        # compute s1's frequency
        s1_freq = [0 for _ in range(26)]
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        
        # compute initial window slide's frequency
        start = 0
        end = window_size - 1
        s2_length = len(s2)

        window_freq = [0 for _ in range(26)]
        for char in s2[start:end+1]:
            window_freq[ord(char) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if window_freq[i] == s1_freq[i] else 0)
        
        if matches == 26:
            return True
        
        start, end = start+1, end+1

        # sliding
        while end < s2_length:
            # start
            window_freq[ord(s2[start-1]) - ord('a')] -= 1
            if window_freq[ord(s2[start-1]) - ord('a')] == s1_freq[ord(s2[start-1]) - ord('a')]:
                matches += 1
            elif window_freq[ord(s2[start-1]) - ord('a')] + 1 == s1_freq[ord(s2[start-1]) - ord('a')]:
                matches -= 1
            # end
            window_freq[ord(s2[end]) - ord('a')] += 1
            if window_freq[ord(s2[end]) - ord('a')] == s1_freq[ord(s2[end]) - ord('a')]:
                matches += 1
            elif window_freq[ord(s2[end]) - ord('a')] - 1 == s1_freq[ord(s2[end]) - ord('a')]:
                matches -= 1

            if matches == 26:
                return True
            start, end = start+1, end+1
        
        return False