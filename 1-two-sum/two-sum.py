class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:


        hashmap = {}
        for i,num in enumerate(nums) :
            vf = target - num

            if vf in hashmap:
                return [hashmap[vf],i]
            hashmap[num] = i


        