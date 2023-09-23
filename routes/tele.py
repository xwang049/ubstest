import json
import logging
from flask import request
from routes import app
import math

def tele(input_dict):
    ports = input_data["p"]
    m = len(ports)
    stations = input_data["q"]
    n = len(stations)
    k = input_dict["k"]
    length = [1000 for i in range(n)]
    st = [0 for i in range(n)]
    for i in range(n):
        if i:
            st[i] = math.sqrt((stations[i][0] - stations[i-1][0]) * (stations[i][0] - stations[i-1][0]) + (stations[i][1] - stations[i-1][1]) * (stations[i][1] - stations[i-1][1]))
        else:
            st[i] = math.sqrt(stations[i][0] * stations[i][0] + stations[i][1] * stations[i][1])
        for j in range(m):
            dist = math.sqrt((stations[i][0] - ports[i][0]) * (stations[i][0] - ports[i][0]) + (stations[i][1] - ports[i][1]) * (stations[i][1] - ports[i][1]))
            length[i] = min(length[i], dist)
    dp = [0 for i in range(k)]
    for i in range(n):
        for t in range(k - 1): 
            dp[t] = min(dp[t] + st[i], dp[t + 1] + length[i])
        dp[k - 1] = dp[k - 1] + st[i]
    ans = 1000
    for t in range(k): 
        ans = min(ans, dp[t])
    return str(round(ans, 2))
        

@app.route('/teleportation', methods=['GET','POST'])
def teleBuilder():
    input_data = request.get_json()
    # return work()
    return tele(input_data)

input_data = {
   "k": 10,
   "p": [[0, 0], [0, 100], [100, 0], [100, 100]],
   "q": [[1, 0], [1, 100], [ 99, 0], [ 99, 100]]
}
# print(tele(input_data))