import json
import logging

from flask import request

from routes import app
import math

logger = logging.getLogger(__name__)

def calculate_boundaries(data):
    total_investment = sum(item["quantity"]*item["price"] for item in data)
    angles = []
    start_angle = 0.0

    for item in sorted(data, key = lambda x:x["quantity"] *x["price"], reverse=True):
        slice_angle = (item["quantity"] * item["price"] /total_investment)*2*math.pi
        if slice_angle < 0.00314159:
            slice_angle = 0.00314159

        angles.append('{:.8f}'.format(start_angle))
        start_angle += slice_angle
    angles.append('{:.8f}'.format(start_angle))
    return angles
# formatted_value = '{:.8f}'.format(value)

@app.route('/pie-chart', methods=['POST'])
def pie():
    All = request.get_json()
    part = All.get("part")
    data = All.get("data")
    if part =="FIRST":
        
        result_data = {
        "instruments": calculate_boundaries(data)
        }
        return  json.dumps(result_data)
    # return json.dumps(greedyM(w,v,f))
