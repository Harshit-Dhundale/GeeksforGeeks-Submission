
from typing import List


class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        orders = [(arr[i], brr[i], arr[i] - brr[i]) for i in range(n)]
        orders.sort(key=lambda x: abs(x[2]), reverse=True)
        
        total_tip = 0
        a_count, b_count = 0, 0
        
        for a_tip, b_tip, diff in orders:
            if (diff >= 0 and a_count < x) or b_count >= y:
                total_tip += a_tip
                a_count += 1
            else:
                total_tip += b_tip
                b_count += 1
        
        return total_tip


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends