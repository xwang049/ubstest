from flask import Flask

app = Flask(__name__)

import routes.lazy
import routes.square1