from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from models.CharityActivity import charity_activity_db
from models.CharityActivityTag import charity_activity_tag_db
from models.User import user_db
from models.UserFavourite import user_fav_db

from routes.RecommenderRoutes import RecommenderRoutes

app: Flask = Flask(__name__)
app.config.from_object("config")

CORS(app)

charity_activity_db.init_app(app)
charity_activity_tag_db.init_app(app)
user_db.init_app(app)
user_fav_db.init_app(app)

with app.app_context():
    charity_activity_db.create_all()
    charity_activity_tag_db.create_all()
    user_db.create_all()
    user_fav_db.create_all()

app.register_blueprint(RecommenderRoutes, url_prefix = "")

if __name__ == "__main__":
    app.debug = True
    app.run()
