from flask import Flask, request, jsonify
from flask_cors import CORS

# Import models
# from models import

# Import Database
from connection import db


# Create the app
def create_app():
    app = Flask(__name__, static_folder='client')
    CORS(app)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # from routes import 

    # Register the routes
    # app.register_blueprint(posts, url_prefix='/api/posts')

    with app.app_context():
        db.create_all()

    return app

# Run the app
app = create_app()


# Start the server
if __name__ == '__main__':
    app.run(debug=True)