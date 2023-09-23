# import numpy as np

# def RailwayCount(input_list):
#     m = input_list[0]
#     n = input_list[1]
#     trlen = np.array(input_list[2:])
#     dp = np.zeros(m + 1, dtype=int)
#     dp[0] = 1
#     for id in range(n):
#         mul = 1
#         tmp = np.zeros(m + 1, dtype=int)
#         while 1:
#             now = mul * trlen[id]
#             if now > m: 
#                 break
#             for i in range(m - now + 1):
#                 tmp[i + now] += dp[i]
#             mul += 1
#         for i in range(m + 1): 
#             dp[i] += tmp[i]
        
#     return dp[m]

# def Work(testlist):
#     ans = []
#     for str in testlist:
#         str_array = str.split(',')
#         for i in range(len(str_array)):
#             str_array[i] = int(str_array[i])
#         ans.append(RailwayCount(str_array))
#     return ans

# testlist = [
#   "5, 3, 2, 1, 4",
#   "3, 3, 4, 1, 2",
#   "11, 1, 2"
# ]
# ans = Work(testlist)
# print(ans)