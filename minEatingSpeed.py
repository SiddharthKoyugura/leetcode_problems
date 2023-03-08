import math

def minEatingSpeed( piles, h):
        low, high = 1, max(piles)
        while low <= high:
            k = (low + high) // 2
            if sum(math.ceil(1.0 * pile / k) for pile in piles) > h:
                  low = k + 1
            else:
                  high = k - 1
        return low

# Time Complexity: O(logn)
# Space Complexity: O(1)

# print(minEatingSpeed([3,6,7,11], 8))
# print(minEatingSpeed([30,11,23,4,20], 5))
# print(minEatingSpeed([30,11,23,4,20], 6))
