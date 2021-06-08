# Minimum number of jumps
'''
Given an array of N integers arr[] where each element 
represents the max number of steps that can be made 
forward from that element. Find the minimum number of 
jumps to reach the end of the array (starting from the 
first element). If an element is 0, then you cannot 
move through that element.
'''
class Solution:
	def minJumps(self, arr, n):
	    if n<1:
	        return 0
	    if arr[0]==0:
	        return -1
	    
	    maxReach = arr[0]
	    steps= arr[0]
	    jump = 1
	    
	    for i in range(1,len(arr)):
	        if i == len(arr)-1:
	            return jump
	        
	        maxReach = max(maxReach, i+arr[i])
	        steps-=1
	        
	        if steps == 0:
	            jump+=1
	            if i>=maxReach:
	                return -1
	            steps = maxReach-i
	    return -1