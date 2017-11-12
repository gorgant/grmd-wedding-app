import os
from flask import Flask, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Guest

app = Flask(__name__)

#Ensure we use correct environment
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#pull the database URI from the app config settings
dbURI = app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(dbURI)

#initialize a database session
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

newGuest = Guest(first_name="Frank",last_name="Pony")
session.add(newGuest)
session.commit()

@app.route('/')
def hello():
    guest = session.query(Guest).first()
    guestList = session.query(Guest).all()
    return jsonify(Guest=[i.serialize for i in guestList])

if __name__ == '__main__':
    app.run()