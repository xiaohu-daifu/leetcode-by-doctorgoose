class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            a = target - num
            if a in hashMap:
                return [hashMap.get(a), idx]
            else:
                hashMap[num] = idx
            

        