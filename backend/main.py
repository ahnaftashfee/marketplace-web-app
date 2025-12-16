"""Main Flask application entry point for the Marketplace backend."""

from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from user import user_bp
from items import items_bp

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    CORS(app)          # allow frontend to call backend jj
    Swagger(app)       # your Swagger docs

    # Register blueprints (these expose /api/login, /api/users, /api/items, etc.)
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(items_bp, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def home():
        """Root route to verify API status."""
        return jsonify({"message": "Marketplace API is running successfully"})
    return app

if __name__ == "__main__":
    application = create_app()
    # listen on all interfaces inside the container
    application.run(host="0.0.0.0", port=5001, debug=True)
