import sys


arr = []
maxSum= -9 * 7
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
for i in range(6):
    for j in range(6):
        if j+2<6 and i+2<6:
            sum1= arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            #print(sum1)
            if sum1>maxSum:
                maxSum=sum1
print(maxSum)
