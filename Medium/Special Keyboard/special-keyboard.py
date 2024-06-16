#User function Template for python3
class Solution:
    def optimalKeys(self, N):
        # code here
        
        if N < 5:
            
            return N
        
        dp = [0] * (N+1)
        
        
        
        dp[1] = 1
        
        dp[2] = 2
        
        dp[3] = 3
        
        dp[4] = 4
        
        for i in range(5,N+1):
            
            dp[i] = dp[i-1] +1
            
            for y in range(3, i-2):
                
                dp[i] = max(dp[i], dp[i-y]*(y-1))
            
            
            
        #print(dp)
            
            
        return dp[N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.optimalKeys(N))
# } Driver Code Ends