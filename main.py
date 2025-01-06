from flask import Flask
from flask_restful import Api

from apis import register_apis
from routes import register_blueprints
from services import db

app = Flask(
    __name__,
    template_folder="views",
    static_folder="public",
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'production'

db.init_app(app)
api = Api(app)
register_blueprints(app)
register_apis(api)


if __name__ == "__main__":
    app.run(debug=True)
    