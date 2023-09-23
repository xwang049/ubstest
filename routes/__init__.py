from flask import Flask

app = Flask(__name__)


import routes.railway
import routes.monkey
import routes.swissbyte
import routes.calendar
import routes.chinesewall
# import routes.bikes
import routes.pie