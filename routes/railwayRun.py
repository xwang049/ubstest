# import json
# import logging
# from flask import request
# import numpy 
# from routes import app

# logger = logging.getLogger(__name__)

# from routes import Railway

# @app.route('/railway-builder', methods=['GET','POST'])
# def railwayBuilder():
#     data = request.get_json()
    
#     Railway.Work(data)
#     # return [1,2,3,4]
#     return json.dumps(Railway.Work(data))
#     # return json.dumps([1,2,3,4])