class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for char in s:
            if 'A'<= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
        