import json
import logging

from flask import request

from routes import app
from routes import lazy_developer1

logger = logging.getLogger(__name__)


@app.route('/lazy-developer', methods=['GET','POST'])
def hi():
    data = request.get_json()
    classes = data.get("classes")
    statements = data.get("statements")
    # return classes
    return lazy_developer1.getNextProbableWords(classes=classes,
                         statements=statements)

    # return json.dumps(data)





