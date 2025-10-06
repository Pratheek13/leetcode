class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # to store number -> index mapping
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
