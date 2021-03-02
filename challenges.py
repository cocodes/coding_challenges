# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:

#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0;
        n = len(nums);
        for num in nums:
            if(num!=0):
                nums[j] = num
                j += 1

        for x in range(j, n):
            nums[x] = 0

s = Solution()
s.moveZeroes([0,2,0,1,4])
# 2,1,4,0,0

# Time Complexity: 0(2*N) = 0(N)
# Space Complexity: 0(1)