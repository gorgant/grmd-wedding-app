import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *

def create_dummy_user():
  newGuest = Guest(first_name="Frank",last_name="Pony")
  db.session.add(newGuest)
  db.session.commit()

@app.route('/')
def home():
    create_dummy_user()
    guest = db.session.query(Guest).first()
    guestList = db.session.query(Guest).all()
    return jsonify(Guest=[i.serialize for i in guestList])

if __name__ == '__main__':
    app.run()