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

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
# 	    maxarea = 0
# 	    l = 0
# 	    r = len(height)-1

# 	    while(l<r):
# 		    maxarea = max(maxarea, min(height[l],height[r])*(r-l))
# 		    if(height[l]<height[r]):
# 			    l+=1
# 		    else:
# 			    r-=1
# 	    return maxarea

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

# Day 7 - Find first and last position of Element in Sorted Array
#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

# Day 8 - Missing Number
# given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = n*(n+1)/2

        return int(intendedSum-currentSum)


# Day 9 - Count Primes
# Count the number of prime numbers less than a non-negative number, n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<2):
            return 0;
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if( isPrime[i] ):
                for multiples_of_i in range(i*i,n,i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)

# Day 10 - Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)


# Day 11 - House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        

# Day 12 - Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0

        for i,price in enumerate(prices):
            if(buyPrice>price):
                buyPrice = price
            else:
                profit = max(profit, price-buyPrice)

        return profit

# Day 13 - Min Stack
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        curMin = self.genMin()

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Day 15 - Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

# Day 16 - First bad version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        

# Day 17 - Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        