class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s.strip().lower() if char.isalnum())
        status = True
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                status = False

        return status
