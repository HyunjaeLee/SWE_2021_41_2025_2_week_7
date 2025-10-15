from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    mp = dict()
    for i, x in enumerate(nums):
        y = target - x
        if y in mp:
            return [mp[y], i]
        mp[x] = i
