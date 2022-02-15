from flask import Flask
import resources.meetup as API
from db import db
from ma import ma

app = Flask(__name__)
app.secret_key = "keep calm"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

app.register_blueprint(API.bp)
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
