import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
from routes import GreedyMonkey
from routes import lazy_developer1
from routes import Railway
@app.route('/greedymonkey', methods=['GET','POST'])
def greedymonkey():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")

    return json.dumps(GreedyMonkey.greedyM(w,v,f))



@app.route('/lazy-developer', methods=['GET','POST'])
def hi():
    data = request.get_json()
    classes = data.get("classes")
    statements = data.get("statements")
    # return classes
    return lazy_developer1.getNextProbableWords(classes=classes,
                         statements=statements)

    # return json.dumps(data)


