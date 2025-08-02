class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index, value in enumerate(nums):
            com = target - value

            if com in d:
                cind = d[com]
                return [index, cind]
            else:
                d[value] = index
