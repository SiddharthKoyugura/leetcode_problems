# Input : nums = [2, 7, 5, 11, 15], target: 9
# Output: [0,1] (2+7=9)


# Logic:
# Create a dictionary(hashMap).
# iterate len(nums) times
# Create a compliment variable, if the compliment key is present in the hashMap then return the indices else add the num as a into the hashmap with its index as a value



from ast import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            compliment = target-nums[i]
            if hashMap.get(compliment):
                return [i, hashMap[compliment]-1]
            hashMap[nums[i]] = i+1


# Time Complexity: O(n)
# Space Complexity: O(n) 