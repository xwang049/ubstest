import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)
@app.route('/chinese-wall', methods=['POST'])
def wall():
    res = {
  "1": "Fluffy",
  "2": "Galactic",
  "3": "password3",
  "4": "password4",
  "5": "password5"
}
    return json.dumps(res)
