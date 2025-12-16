"""User-related API routes for the Marketplace application."""
# pylint: disable=duplicate-code
import sqlite3
from flask import Blueprint, jsonify, request

user_bp = Blueprint("user_bp", __name__)

# ───────────────────────────────
#  Add a new user
# ───────────────────────────────
@user_bp.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the database."""
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        seller_id = data.get("seller_id")

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password, seller_id) VALUES (?, ?, ?)",
            (username, password, seller_id),
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "User added successfully"}), 201
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500


# ───────────────────────────────
#  Get all users
# ───────────────────────────────
@user_bp.route("/users", methods=["GET"])
def get_users():
    """Retrieve all users from the database."""
    try:
        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        conn.close()

        return jsonify({"users": users})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500


# ───────────────────────────────
#  User login
# ───────────────────────────────
@user_bp.route("/login", methods=["POST"])
def login_user():
    """Validate user credentials."""
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cur.fetchone()
        conn.close()

        if user:
            seller_id = user[1];
            return jsonify({"message": "Login successful", "seller_id": seller_id})
        return jsonify({"message": "Invalid credentials"})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500

@user_bp.route("/orders", methods=["GET"])
def get_orders():
    try:
        seller_id = request.args.get("seller_id")

        # STOP if seller_id is missing or invalid jj
        if seller_id is None or seller_id == "" or seller_id == "null":
            return jsonify({"orders": []})

        seller_id = int(seller_id)

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders WHERE seller_id = ?", (seller_id,))
        orders = cur.fetchall()
        conn.close()

        return jsonify({"orders": orders})

    except Exception as err:
        print("ERROR IN /orders:", err)
        return jsonify({"error": str(err)}), 500
    

@user_bp.route("/add_order", methods=["POST"])
def add_order():
    """Add a new order to the database."""
    try:
        data = request.get_json()
        buyer_id = data.get("buyer_id")
        seller_id = data.get("seller_id")
        item_id = data.get("item_id")
        total = data.get("total")

        if not buyer_id or not seller_id or not item_id or not total:
            return jsonify({"error": "Missing fields"}), 400

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO orders (buyer_id, seller_id, item_id, total) VALUES (?, ?, ?, ?)",
            (buyer_id, seller_id, item_id, total)
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Order added successfully"}), 201

    except Exception as err:
        return jsonify({"error": str(err)}), 500

@user_bp.route("/buyer_orders", methods=["GET"])
def get_buyer_orders():
    """Retrieve all orders for a given buyer."""
    try:
        buyer_id = request.args.get("buyer_id")

        if not buyer_id:
            return jsonify({"orders": []}), 200

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM orders WHERE buyer_id = ?", (buyer_id,))
        orders = cur.fetchall()
        conn.close()

        return jsonify({"orders": orders}), 200

    except Exception as err:
        return jsonify({"error": str(err)}), 500
