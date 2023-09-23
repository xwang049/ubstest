import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
from routes import GreedyMonkey

@app.route('/greedymonkey', methods=['GET','POST'])
def greedymonkey():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")

    return json.dumps(GreedyMonkey.greedyM(w,v,f))



