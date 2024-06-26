from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        ans = []
        for i in nums2:
            if count[i]  > 0:
                count[i] -= 1
                ans.append(i)

        return ans