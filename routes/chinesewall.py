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
  "3": "mangoes",
  "4": "Subatomic",
  "5": "party"
}
    return json.dumps(res)
