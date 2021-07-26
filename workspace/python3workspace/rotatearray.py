from typing import List

def reverse(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start,end = start+1,end-1

def rotatearray(testcases) -> List[int]:

    #"Write your code here and run with testHarness"
    nums,k = testcases['nums'],testcases['k']
    n = len(nums)
    k %= n
    
    # reverse(nums,0,n-1)
    # reverse(nums,0,k-1)
    # reverse(nums,k,n-1)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
    # return []
