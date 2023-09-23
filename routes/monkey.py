import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)

def greedyM(w, v, flist):
    flen = len(flist)
    dp = [[0 for i in range(v + 1)] for j in range(w + 1)]
    ans = 0
    for id in range(flen):
        for i in range(w, -1, -1):
            for j in range(v, -1, -1):
                nxti = i + flist[id][0]
                nxtj = j + flist[id][1]
                if nxti > w or nxtj > v:
                    continue
                dp[nxti][nxtj] = max(dp[nxti][nxtj], dp[i][j] + flist[id][2])
    for i in range(w + 1):
        for j in range(v + 1):
            ans = max(ans, dp[i][j])
    return ans





@app.route('/greedymonkey', methods=['POST'])
def greedymonkey():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")
    return json.dumps(greedyM(w,v,f))
