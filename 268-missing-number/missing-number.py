class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor1,xor2=0,0
        for i in range(n):
            xor1=xor1^nums[i]
            xor2=xor2^(i+1)
        return xor1^xor2