from flask import Flask
from flask_cors import CORS

from routes.chat import chatbot_route
from routes.search import search_route
from routes.auth import auth_route
from routes.history import history_route

app = Flask(__name__)

# ✅ Improved CORS configuration
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Register all routes
app.register_blueprint(chatbot_route)
app.register_blueprint(search_route)
app.register_blueprint(auth_route)
app.register_blueprint(history_route)

# ✅ Safe backend startup
if __name__ == '__main__':
    app.run(port=5001, debug=False, use_reloader=False)