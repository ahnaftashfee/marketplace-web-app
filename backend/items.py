"""Item-related API routes for the Marketplace application."""
# pylint: disable=duplicate-code
import sqlite3
from flask import Blueprint, jsonify, request

items_bp = Blueprint("items_bp", __name__)

# ───────────────────────────────
#  Add a new item
# ───────────────────────────────
@items_bp.route("/add_item", methods=["POST"])
def add_item():
    """Add a new item to the database."""
    try:
        data = request.get_json()
        item_id = data.get("item_id")
        seller_id = data.get("seller_id")
        name = data.get("title")
        price = data.get("price")
        description = data.get("description")


        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO items (id, title, price, description, seller_id) VALUES (?, ?, ?, ?, ?)",
            (item_id, name, price, description, seller_id),
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Item added successfully"}), 201
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500


# ───────────────────────────────
#  Get all items
# ───────────────────────────────
@items_bp.route("/items", methods=["GET"])
def get_items():
    """Retrieve all items from the database."""
    try:
        seller_id = request.args.get("seller_id")

        if seller_id is None or seller_id == "" or seller_id == "null":
            return jsonify({"items": []})

        seller_id = int(seller_id)

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM items WHERE seller_id = ?", (seller_id,))
        items = cur.fetchall()
        conn.close()

        return jsonify({"items": items})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500
    
@items_bp.route("/all_items", methods=["GET"])
def get_all_items():
    """Retrieve all items from the database."""
    try:
        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM items")
        items = cur.fetchall()
        conn.close()
        
        return jsonify({"items": items})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500

#   GET ONE ITEM ONLY

@items_bp.route("/item/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """Retrieve a singular item from the database"""
    try:

        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute(""" 
                            SELECT i.id, i.title, i.price, i.description, i.seller_id, u.username, u.id AS custom_seller_id
                            FROM items i
                            JOIN users u ON i.seller_id = u.seller_id
                            WHERE i.id = ?"""
        , (item_id,))
        item = cur.fetchone()
        conn.close()

        item = {
            "id": item[0],
            "title": item[1],
            "price": item[2],
            "description": item[3],
            "seller_id": item[4],
            "seller_custom_id": item[6],
            "seller_username": item[5]
        }

        return jsonify({"item": item})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500


# ───────────────────────────────
#  Delete an item jj
# ───────────────────────────────
@items_bp.route("/delete_item/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete an item from the database."""
    try:
        conn = sqlite3.connect("marketplace.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Item deleted successfully"})
    except sqlite3.Error as err:
        return jsonify({"error": str(err)}), 500
