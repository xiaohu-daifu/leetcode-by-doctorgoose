class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            a = target - num
            if a in nums:
                try:
                    bleb = nums.index(a, nums.index(num) + 1)
                    return [nums.index(num), bleb]
                except ValueError:
                    continue

        