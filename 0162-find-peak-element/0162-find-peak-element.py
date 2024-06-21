class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak_element = max(nums)
        
        return (nums.index(peak_element))