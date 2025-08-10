class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0
        for money in nums:
            temp = max(house1+money, house2)
            house1 = house2
            house2 = temp
        return house2