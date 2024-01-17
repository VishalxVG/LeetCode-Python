# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Brute Force Approach 

class Solution:
    def containsDuplicate(nums) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution.containsDuplicate(nums))