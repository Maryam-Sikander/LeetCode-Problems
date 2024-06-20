class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [i for i, num in enumerate(nums) if num == target]

        if len(result) >= 2:
            return (result[0], result[-1])
        elif len(result) == 1:
            return (result[0], result[0])
        else:
            return [-1,-1]