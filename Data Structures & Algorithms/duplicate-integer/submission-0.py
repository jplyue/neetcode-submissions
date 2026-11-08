class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = {}
        result = False

        for i in range(0, len(nums)):
            if nums[i] not in val:
                val[nums[i]] = 1
            else:
                result = True

        return result
