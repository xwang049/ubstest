import json
import logging
from flask import request
from routes import app
logger = logging.getLogger(__name__)

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

@app.route('/digital-colony', methods=['GET','POST'])
def colonyBuilder():
    data = request.get_json()
    # decode_data = data.decode('utf-8')
    # list1 = decode_data[1:-1].split(", ")
    return json.dumps(work(data))
