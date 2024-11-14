class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []

        for word in title.split():
            if len(word) < 3:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        return " ".join(result)