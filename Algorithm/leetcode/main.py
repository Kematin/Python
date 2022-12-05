from typing import List

# Two Sum (Easy)
# My solution (N^2)
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums[::-1]:
                if i + j == target and nums.count(j)>=2 and i == j:
                    first_item = nums.index(j)
                    nums[nums.index(j)] = -1
                    second_item = nums.index(j)
                    return [first_item, second_item]

                elif i + j == target and i != j: 
                    return [nums.index(i), nums.index(j)]

# Another solution (N, hashmap)
class Solution_1_A:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i + 1
            else:
                return map[nums[i]], i+1

        return -1, -1


def start():
    pass

start()
