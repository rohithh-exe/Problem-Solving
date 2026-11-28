class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        checker = set(nums)
        return bool(len(nums) != len(checker))

        