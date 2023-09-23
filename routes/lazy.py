import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/lazy', methods=['GET','POST'])
def hi():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    class_definitions = data.get("input",{})
    result = class_definitions
    logging.info("My result :{}".format(result))
    return json.dumps(result)
    # input_data = request.get_json().get('input', {})
    # return jsonify({"message": "Input data stored successfully."})