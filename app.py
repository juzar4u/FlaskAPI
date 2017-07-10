import flask
import flask_sqlalchemy
import flask_restless

app = flask.Flask(__name__)


ip = "172.16.3.97"
db = "akhbaar24"
pwd = "danat123$"
user = "akhbaar24user"


app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://akhbaar24user:danat123$@172.16.3.97/Akhbaar24"
db = flask_sqlalchemy.SQLAlchemy(app)

class Menus(db.Model):
        MenuID = db.Column(db.Integer, primary_key=True)
        Name = db.Column(db.Text)
        URL = db.Column(db.Text)


manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Menus, methods=['GET'])

app.run()