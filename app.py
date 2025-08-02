import os
from flask import Flask, request, jsonify
from models import db, Todo
from flask.cli import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Build DB URL from .env values
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Wellcome to home page
@app.route("/")
def home():
    return f"Welcome to the Todo API!"

# Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify([
        {"id": t.id, "text": t.text, "done": t.done} for t in todos
    ])

@app.route("/todos", methods=["POST"])
def add_todo():
    if not request.is_json:
        return jsonify({"error": "request must be JSON"}), 415

    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    new_todo = Todo(text=data["text"])
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"id": new_todo.id, "text": new_todo.text, "done": new_todo.done}), 201


@app.route("/todos/<string:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    todo.text = data.get("text", todo.text)
    todo.done = data.get("done", todo.done)
    db.session.commit()

    return jsonify({"id": todo.id, "text": todo.text, "done": todo.done})


@app.route("/todos/<string:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Todo deleted", "id": todo.id})


if __name__ == '__main__':
    app.run(debug=True)