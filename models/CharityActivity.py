from typing import Any, Dict

from flask_sqlalchemy import SQLAlchemy

charity_activity_db = SQLAlchemy()


class CharityActivity(charity_activity_db.Model):
    __tablename__ = "charity_activity"

    id = charity_activity_db.Column(charity_activity_db.Integer, autoincrement = True, nullable = False, primary_key = True)
    title = charity_activity_db.Column(charity_activity_db.String)
    description = charity_activity_db.Column(charity_activity_db.Text)

    @property
    def jsonable(self) -> Dict[str, Any]: 
        return {
            "id": self.id, 
            "title": self.title, 
            "description": self.description, 
        }