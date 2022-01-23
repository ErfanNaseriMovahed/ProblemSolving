class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = (value for value in sorted(set(nums)))
 '''
convert the list to a set and replace the elements of the list with the elements of the set.
 '''