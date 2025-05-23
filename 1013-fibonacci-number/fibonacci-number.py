from functools import cache
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def f(n):
            if n==0:
                return 0
            if n==1:
                return 1
            else:
                return f(n-1)+f(n-2)
        return f(n)
