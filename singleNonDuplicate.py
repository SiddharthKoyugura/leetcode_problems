# Approach: 1

def singleNonDuplicate(nums):
    plot = nums[0]
    for i in range(len(nums)):
        if nums[i] != plot:
            return plot
        elif (i+1)%2==0:
          plot = nums[i+1]
        else:
            plot = nums[i]
    return plot

## Time Complexity: O(n)
## Space Complexity: O(1)



# Approach: 2
def singleNonDuplicate(nums):
    low, high, mid = 0, len(nums)-1, 0
    while low<high:
        mid = (low+high)//2
        division = mid % 2
        if (division == 0 and nums[mid]==nums[mid+1]) or (division == 1 and nums[mid]==nums[mid-1]):
            low = mid+1
        else:
            high = mid
    return nums[low]

## Time Complexity: O(logn)
## Space Complexity: O(1)