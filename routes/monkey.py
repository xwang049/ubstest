import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def greedyM(w, v, flist):
    # flen = len(flist)
    # dp = [[0 for i in range(v + 1)] for j in range(w + 1)]
    # ans = 0
    # for id in range(flen):
    #     for i in range(w, -1, -1):
    #         for j in range(v, -1, -1):
    #             nxti = i + flist[id][0]
    #             nxtj = j + flist[id][1]
    #             if nxti > w or nxtj > v:
    #                 continue
    #             dp[nxti][nxtj] = max(dp[nxti][nxtj], dp[i][j] + flist[id][2])
    # for i in range(w + 1):
    #     for j in range(v + 1):
    #         ans = max(ans, dp[i][j])
    # return ans

    n = len(flist)
    dp = [[0] * (v + 1) for _ in range(w + 1)]

    for i in range(n):
        weight, volume, value = flist[i]
        for w in range(w, weight - 1, -1):
            for v in range(v, volume - 1, -1):
                dp[w][v] = max(dp[w][v], dp[w - weight][v - volume] + value)

    return dp[w][v]





@app.route('/greedymonkey', methods=['POST'])
def greedymonkey():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")
    return json.dumps(greedyM(w,v,f))
