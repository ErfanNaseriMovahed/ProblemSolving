class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

'''
As long as val is included in nums, remove it. The function on the website will automatically return length of nums.
'''