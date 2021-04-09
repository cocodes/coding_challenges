# Day 4 - Valid Moutain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A)<3):
            return False
        
        i = 1
        while(i<len(A) and A[i]>A[i-1]):
            i+=1
        
        if(i==1 or i==len(A)):
            return False
        
        while(i<len(A) and A[i]<A[i-1]):
            i+=1
        
        return i==len(A)

# Day 5 - Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        