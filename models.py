"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image = "https://www.shutterstock.com/image-vector/user-profile-icon-trendy-flat-design-1923506948"

class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=default_image)

def full_name(self):
    return f"{self.first_name} {self.last_name}"


def connect_db(app):
    db.app = app
    db.init_app(app)


    