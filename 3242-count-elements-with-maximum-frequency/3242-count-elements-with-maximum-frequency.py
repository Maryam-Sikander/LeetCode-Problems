from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())

        total_count = sum(freq for num, freq in count.items() if freq == max_freq)

        return total_count
