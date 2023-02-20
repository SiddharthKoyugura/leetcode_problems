#### Approach 1:

def searchInsert(nums, target):
    n = len(nums)
    for i in range(n):
        if (nums[i]==target) or (nums[i]>target):
            return i
    return n

# Time Complexity: O(n)
# Space Complexity: O(1)

#########################################################################################################

#### Approach 2:
def searchInsert(nums, target):
    n = len(nums)
    if n==0: return 0
    low, high, mid = 0, n-1, 0
    while low<=high:
        mid = (low+high)//2
        x = nums[mid]
        if(x==target): return mid
        elif(x>target): high = mid-1
        elif(x<target): low = mid+1

    if nums[mid]>target: return mid
    return mid+1

# Time Complexity: O(logn)
# Space Complexity: O(1)