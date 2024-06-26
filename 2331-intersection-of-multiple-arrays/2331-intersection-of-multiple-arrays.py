class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersection_list = set(nums[0])

        for i in range(len(nums)):
            intersection_list.intersection_update(nums[i])
        return list(sorted(intersection_list))