from flask import Blueprint
from controllers.Recommender import Recommender

RecommenderRoutes = Blueprint("RecommenderRoutes", __name__)

RecommenderRoutes.get("/activities")
RecommenderRoutes.get("/")
RecommenderRoutes.get("/activities")