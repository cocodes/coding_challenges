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
		maxarea = 0
		l = 0
		r = len(height)-1

		while(l<r):
			maxarea = max(maxarea, min(height[l],height[r])*(r-l))
			if(height[l]<height[r]):
				l+=1
			else:
				r-=1
		return maxarea

# Day 6 - Longest substring without repeating characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while(left<n and right<n):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right
            ans = max(ans,right-left+1)
            right+=1
        return ans