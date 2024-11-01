from flask import Flask

from app.db import create_db
from app.routes import position_route, user_route, post_route
from app.data.password import ADMIN_PASS


app = Flask(__name__)
app.secret_key = ADMIN_PASS
app.register_blueprint(position_route)
app.register_blueprint(user_route)
app.register_blueprint(post_route)


def main():
    create_db()
    app.run(debug=True)