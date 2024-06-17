class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        # extend nums1 with nums2 and sort
        nums1.extend(nums2)
        nums1.sort()
        