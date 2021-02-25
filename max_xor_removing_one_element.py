def maxXOR(arr, n): 
    xorArr = 0
    for i in range(n): 
        xorArr ^= arr[i] 
    ans = 0
    for i in range(n): 
        ans = max(ans, (xorArr ^ arr[i]))  
    return ans 
  
arr = list(map(int, input().split()))
n = len(arr) 
print(maxXOR(arr, n)) 
