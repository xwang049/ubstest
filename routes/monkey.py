import json
import logging

from flask import request

from routes import app
from routes import lazy_developer

logger = logging.getLogger(__name__)


@app.route('/greedymonkey', methods=['GET','POST'])
def greedymonkey():
    data = request.get_json()
    w = data.get("w")
    v = data.get("v")
    f = data.get("f")

    return 0



