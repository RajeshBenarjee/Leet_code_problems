class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if self.arr:
            self.arr.sort()
            n = len(self.arr)
            if n % 2 == 1:
                return self.arr[n // 2]
            else:
                return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
        else:
            return None

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()