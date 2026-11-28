class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1
        for i in range(len(arr)-1,-1,-1):
            original = arr[i]
            arr[i] = maximum
            maximum = max(maximum,original)
        return arr