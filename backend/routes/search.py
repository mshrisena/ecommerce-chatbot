from flask import Blueprint, request, jsonify
from database.connection import get_db_connection

search_route = Blueprint('search_route', __name__)

@search_route.route('/products/search')
def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{query}%",)).fetchall()
    conn.close()
    result = [{
        "id": p["id"],
        "name": p["name"],
        "price": p["price"],
        "description": p["description"],
        "image_url": p["image_url"]
    } for p in products]
    return jsonify(result)
