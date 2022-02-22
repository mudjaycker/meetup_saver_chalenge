from flask import Flask
import resources.meetup as API
from instances.db import db
from instances.ma import ma

#? if getting No 'Access-Control-Allow-Origin' header is present on the requested resource. 
#? Origin 'null' is therefore not allowed access. error in your browser's console
#! make sure to install flask_cors, then import CORS from it as below and link it  with your app 
#& like cors = CORS(app) 

from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
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