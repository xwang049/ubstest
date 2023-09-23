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

def Work(test_dict):
    return greedyM(test_dict["w"], test_dict["v"], test_dict["f"])

test_dict = {
  "w": 100,
  "v": 150,
  "f": [
    [60, 70, 60],
    [30, 80, 40],
    [35, 70, 70]
  ]
}

ans = Work(test_dict)
print(ans)