from flask import Flask

app = Flask(__name__)

import routes.lazy
import routes.square1
import routes.monkey
import routes.railwayRun
import routes.colony
import routes.Railway