import React, { useState, useEffect } from "react";
import axios from "axios";
import "./base.css";
import "./seller.css";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";

export default function Seller() {
//jj

    const seller_id = localStorage.getItem("seller_id");
    console.log("SELLER ID =", seller_id);

    const [form, setForm] = useState({ seller_id: "", title: "", description: "", price: "" });
    const [message, setMessage] = useState("");
    const [searchTerm, setSearchTerm] = useState("");
    const [items, setItems] = useState([]);
    const [orders, setOrders] = useState([]);

    const handleSearch = () => {
        window.location.href = "/search";
    };

    const handleLogOut = () => {
        localStorage.removeItem("seller_id");
        window.location.href = "/";
    };

    const handleNewItem = async () => {
        const item_id = Math.floor(100000000 + Math.random() * 900000000);
        const title = prompt("Enter the item title:");
        const description = prompt("Enter the item description:");
        const price = prompt("Enter the item price:");

        if (!seller_id || !title || !price) {
            alert("Seller ID, title, and price cannot be empty.");
            return;
        }

        try {
            const res = await axios.post(`${API_BASE_URL}/api/add_item?seller_id=${seller_id}`, {
                item_id: item_id,
                seller_id: seller_id,
                title: title,
                description: description,
                price: price
            });

            if (res.data.message) {
                setMessage("Item added successfully!");
            } else {
                setMessage("Failed to add item. Please try again.");
            }
        } catch (error) {
            setMessage("An error occurred. Please try again.");
        }
    };

    const handleRemoveItem = async (item_id) => {
        try {
            const res = await axios.delete(`${API_BASE_URL}/api/delete_item/${item_id}`);
        } catch (error) {
            console.error("Error removing item:", error);
        }
        fetchItems();
    };

    const fetchItems = async () => {
        try {
            const res = await axios.get(`${API_BASE_URL}/api/items?seller_id=${seller_id}`);
            setItems(res.data.items);
        } catch (error) {
            console.error("Error fetching items:", error);
        }
    };

    //jj

    const fetchOrders = async () => {
        try {
            const res = await axios.get(`${API_BASE_URL}/api/orders?seller_id=${seller_id}`);
            setOrders(res.data.orders);
        } catch (error) {
            console.error("Error fetching orders:", error);
        }
    };

    useEffect(() => {
        fetchItems();
        fetchOrders();
    }, []);

    return (
        <div className="seller-container">
            <header className="navbar">
                <button className="account" onClick={handleLogOut}>Log Out</button>
                <h1 className="logo">Marketplace</h1>

                <div className="search-bar">
                    <input
                        type="text"
                        placeholder="Search the Marketplace"
                        className="search"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                    <button className="search-btn" onClick={handleSearch}>
                        Search
                    </button>
                </div>

                <a href="/cart" className="cart-btn">Open Cart</a>
            </header>

            <main className="content">
                <h2>Welcome to your Seller Homepage</h2>

                <button className="add-item-btn" onClick={handleNewItem}>
                    Add New Item
                </button>

                <h2>Your Items</h2>
                <ul>
                    {items.map(item => (
                        <li key={item[0]}>
                            <p><b>{item[2]}</b></p>
                            <p>{item[3]}</p>
                            <p>Price: ${item[4]}</p>
                            <button onClick={() => handleRemoveItem(item[0])}>Remove Item</button>
                        </li>
                    ))}
                </ul>

                <h3>Requests</h3>
                <ul>
                    {orders.map(order => (
                        <li key={order[0]}>
                            <p>Order ID: {order[0]}</p>
                            <p>Buyer ID: {order[1]}</p>
                            <p>Seller ID: {order[2]}</p>
                            <p>Item ID: {order[3]}</p>
                            <p>Total: ${order[4]}</p>
                        </li>
                    ))}
                </ul>
            </main>
        </div>
    );
}
