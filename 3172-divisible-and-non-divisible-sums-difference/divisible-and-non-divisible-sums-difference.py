class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # T(N)=O(N) S(N)=O(1)
        nums1=0
        nums2=0
        for i in range(1,n+1):
            if i%m==0:
                nums2+=i
            else:
                nums1+=i
        return nums1-nums2