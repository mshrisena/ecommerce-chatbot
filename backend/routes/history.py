from flask import Blueprint, request, jsonify
from database.connection import get_db_connection

history_route = Blueprint('history_route', __name__)

@history_route.route('/chat/history')
def chat_history():
    user_id = request.args.get('user_id', 'guest')
    conn = get_db_connection()
    history = conn.execute("SELECT * FROM chat_history WHERE user_id=? ORDER BY timestamp DESC LIMIT 20", (user_id,)).fetchall()
    conn.close()
    return jsonify([
        {"message": h["message"], "response": h["response"], "timestamp": h["timestamp"]}
        for h in history
    ])
