class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s=s.reverse()
        # S(N)=O(N) 
        l=0
        r=len(s)-1
        while l<=r:
            (s[l],s[r])=(s[r],s[l])
            l+=1
            r-=1
        # T(N)=O(N//2) S(N)=O(1)
        