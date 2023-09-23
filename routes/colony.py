import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/digital-colony', methods=['GET','POST'])
def colony1():
    data = request.get_json()

    # input_value = data.get("input")
    work(data)
    return json.dumps(work(data))

def colony(inputdict):
    ststr = inputdict['colony']
    gen = inputdict['generations']
    dp = [[0 for i in range(10)] for j in range(10)]
    tmp = [[0 for i in range(10)] for j in range(10)]
    sum = 0
    for i in range(3):
        dp[int(ststr[i])][int(ststr[i + 1])] += 1
        sum += int(ststr[i])
    sum += int(ststr[3])
    for id in range(gen):
        cur = sum % 10
        for i in range(10):
            for j in range(10):
                nxt = (i - j + cur + 10) % 10
                sum +=  nxt * dp[i][j]
                tmp[i][nxt] += dp[i][j]
                tmp[nxt][j] += dp[i][j]
        for i in range(10): 
            for j in range(10): 
                dp[i][j] = tmp[i][j]
                tmp[i][j] = 0
    return sum

def work(inputlist):
    ans = []
    for x in inputlist:
        ans.append(colony(x))
    #print(ans)
    return ans
                
# inputlist = [
#     { "generations": 10, "colony": "1000" },
#     { "generations": 50, "colony": "1000" },
# ]

# work(inputlist)
# dp[i][j] 相邻的cnt
# 对于一个current sum， 末位转移