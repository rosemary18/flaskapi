from .global_routes import global_routes

def register_blueprints(app):
    app.register_blueprint(global_routes)