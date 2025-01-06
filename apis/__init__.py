from apis.user_api import Users, User

def register_apis(api):
    api.add_resource(Users, '/api/users/')
    api.add_resource(User, '/api/users/<int:id>')