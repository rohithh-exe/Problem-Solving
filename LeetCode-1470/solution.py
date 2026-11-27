class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i,j in zip(range(len(nums)),range(n,len(nums))):
            ans.append(nums[i])
            ans.append(nums[j])
        return ans
        