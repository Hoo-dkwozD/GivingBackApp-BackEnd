from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from models.CharityActivity import charity_activity_db
from models.CharityActivityTag import charity_activity_tag_db

app: Flask = Flask(__name__)
app.config.from_object("config")

charity_activity_db.init_app(app)
charity_activity_tag_db.init_app(app)
