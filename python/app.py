from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# postgresql://scott:tiger@localhost:5432/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']

db = SQLAlchemy(app)

# Model
class Items(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  content = db.Column(db.String(255))

  def __init__(self, title, content):
    self.title = title
    self.content = content

db.create_all()

@app.route('/', methods=['GET'])
def get():
  return "ok"

# Create Item
@app.route('/items', methods=['POST'])
def itemadd():
  request_data = request.get_json()

  title = request_data['title']
  content = request_data['content']

  db.session.add(Items(title, content))
  db.session.commit()

  return "item created"

