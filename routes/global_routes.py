from flask import Blueprint, render_template 

global_routes = Blueprint('global_routes', __name__)

@global_routes.route('/')
def index():
    return render_template('index.html')