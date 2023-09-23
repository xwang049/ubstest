import json
import logging
from flask import request
from routes import app

def greedyM(w, v, flist):
    flen = len(flist)
    dp = [[0 for i in range(v + 1)] for j in range(w + 1)]
    ans = 0
    for id in range(flen):
        xw = flist[id][0]
        xv = flist[id][1]
        for i in range(w - xw, -1, -1):
            for j in range(v - xv, -1, -1):
                nxti = i + xw
                nxtj = j + xv
                dp[nxti][nxtj] = max(dp[nxti][nxtj], dp[i][j] + flist[id][2])
    for i in range(w + 1):
        for j in range(v + 1):
            ans = max(ans, dp[i][j])
    return ans

def Work(test_dict):
    return greedyM(test_dict["w"], test_dict["v"], test_dict["f"])

@app.route('/greedymonkey', methods=['GET','POST'])
def monkeyBuilder():
    data = request.get_json()
    # decode_data = data.decode('utf-8')
    # list1 = decode_data[1:-1].split(", ")
    return json.dumps(Work(data))
