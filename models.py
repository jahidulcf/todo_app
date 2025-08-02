import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class Todo(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid())
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)