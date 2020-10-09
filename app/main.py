from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/messages"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String())

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"<msg {self.message}>"

@app.route('/', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        return process_post(request.json)
    else:
        return 'Hello, World!'

def process_post(data):
    message = Message(message=data['message'])
    db.session.add(message)
    db.session.commit()
    return f"Added {data['message']} to db!"
