import json
import logging
from flask import request
from routes import app

flag = 1
upd = -1
input_data = {}
ans_data = {}

def output(str):
    ans_data = {"playerAction": str}
    flag = 0

def dfs(cur_pos, pt, dirs, ndirs, cur_map):
    #input_dict = output()
    pt[cur_pos] = cur_map
    for i in range(4):
        nxt_id = dirs[i][1]
        nxt_val = cur_map[nxt_id[0]][nxt_id[1]]
        dir = dirs[i][0]
        nxt_pos = (dir[0] + cur_pos[0], dir[1] + cur_pos[1])
        if nxt_val == 3 or nxt_val == 0: 
            continue
        elif nxt_pos in pt:
            continue
        input_dict = output(ndirs[i])
        dfs(nxt_pos, pt, dirs, ndirs, input_dict["nearby"])
        if i < 2:
            output(ndirs[1 - i])
        else:
            output(ndirs[5 - i])
    
def findway(input_dict):
    dirs = (((-1, 0), (1, 0)), ((1, 0), (1, 2)), ((0, 1), (0, 1)), ((0, -1), (2, 1)))
    ndirs = ("left", "right", "up", "down")
    pt = {}
    dfs((0, 0), pt, dirs, ndirs, input_dict["nearby"])
    m = {(0, 0): 0}
    queue_list = [((0, 0), [])]
    queue_pos = 0
    queue_sz = 1
    while queue_pos < queue_sz:
        cur_pos = queue_list[queue_pos][0]
        cur_str = queue_list[queue_pos][1]
        cur_map = pt[cur_pos]
        queue_pos += 1
        for i in range(4):
            nxt_id = dirs[i][1]
            nxt_val = cur_map[nxt_id[0]][nxt_id[1]]
            nxt_str = cur_str + [ndirs[i]]
            if nxt_val == 3: 
                ans = nxt_str
                break
            elif nxt_val == 0: 
                continue
            dir = dirs[i][0]
            nxt_pos = (dir[0] + cur_pos[0], dir[1] + cur_pos[1])
            if nxt_pos in m:
                continue
            m[nxt_pos] = m[cur_pos] + 1
            queue_list.append((nxt_pos, nxt_str))
            queue_sz += 1
    
    for x in ans:
        output(x)
            
def work(input_data):
    if flag == 1:
        flag = -1
        findway()
    else:
        
    while upd == -1:
        continue
    return ans_data

@app.route('/maze', methods=['GET','POST'])
def mazeBuilder():
    input_data = request.get_json()
    # work(input_data)
    # return work()
    return json.dumps(work(input_data))


# @app.route('/pie-chart', methods=['GET','POST'])
# def mazeBuilder():
#     input_data = request.get_json()
#     # return work()
#     return json.dumps(work())