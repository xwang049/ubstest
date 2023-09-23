import json
import logging
from flask import request
from routes import app
logger = logging.getLogger(__name__)

def work():
    return {
                "1": "fluffy",
                "2": "galactic",
                "3": "mangoes",
                "4": "subatomic",
                "5": "party"
            }


@app.route('/chinese-wall', methods=['GET','POST'])
def chineseBuilder():
    # data = request.get_json()
    # decode_data = data.decode('utf-8')
    # list1 = decode_data[1:-1].split(", ")
    return json.dumps(work())
