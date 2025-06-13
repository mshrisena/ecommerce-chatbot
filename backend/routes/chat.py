from flask import Blueprint, request, jsonify
from database.connection import get_db_connection
import datetime



chatbot_route = Blueprint('chatbot_route', __name__)

@chatbot_route.route('/chat', methods=['POST'])
def chat():
    print("🧠 /chat POST hit:", request.json)
    user_input = request.json.get('message')
    user_id = request.json.get('user_id', 'guest')
    response = ""

    if "hello" in user_input.lower():
        response = "Hi! I'm your assistant. What do you want to buy today?"
    elif "laptop" in user_input.lower():
        conn = get_db_connection()
        products = conn.execute("SELECT * FROM products WHERE category='electronics' AND name LIKE '%laptop%'").fetchall()
        response = "Here are some laptops for you Laptops:\n" + "\n".join([f"- {p['name']} (${p['price']})" for p in products]) if products else "No laptops found."
        conn.close()
    else:
        response = "Please specify a product or category."

    # Save chat
    conn = get_db_connection()
    timestamp = datetime.datetime.now().isoformat()
    conn.execute("INSERT INTO chat_history (user_id, message, response, timestamp) VALUES (?, ?, ?, ?)",
                 (user_id, user_input, response, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"response": response})
