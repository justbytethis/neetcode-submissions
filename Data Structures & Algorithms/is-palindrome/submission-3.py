class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([(c if c.isalpha() or c.isdigit() else "") for c in s])
        i = 0
        j = len(s) - 1
        while True:
            if i >= j or i >= len(s) or j < 0:
                break

            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def _is_ignore(self, c: str) -> bool:
        ascii_index = ord(c)
        if (48 <= ascii_index and ascii_index <= 57) or (65 <= ascii_index and ascii_index <= 122):
            return False
        else:
            return True