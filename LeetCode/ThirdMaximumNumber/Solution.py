class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        if n < 3:
            return nums[n-1]
        return nums[n-3]

'''
First, I take out the duplicates by turning the list into a set.
Then, I sort the list and if the list has less than 3 elements, I return the max value of the list.
and if the list contains more than 3 elements, I return the third element from the end of the list.
'''