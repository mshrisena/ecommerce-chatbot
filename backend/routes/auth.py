import sqlite3
from flask import Blueprint, request, jsonify
from database.connection import get_db_connection
import hashlib

auth_route = Blueprint('auth_route', __name__)

@auth_route.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()

    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists"}), 400
    finally:
        conn.close()

    return jsonify({"message": "User registered successfully"})

@auth_route.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
    conn.close()
    if user:
        return jsonify({"message": "Login successful", "user_id": user["id"]})
    return jsonify({"message": "Invalid credentials"}), 401
