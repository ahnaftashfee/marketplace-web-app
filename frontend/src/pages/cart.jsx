import React, { useState, useEffect } from "react";
import "./base.css";
import "./cart.css";

//jj

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";

export default function Cart() {
  const [cartItems, setCartItems] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    const buyer_id = localStorage.getItem("seller_id"); // same login id

    if (!buyer_id) return;

    fetch(`${API_BASE_URL}/api/buyer_orders?buyer_id=${buyer_id}`)
        .then(res => res.json())
        .then(data => setCartItems(data.orders || []))
        .catch(err => console.error("Error fetching buyer orders:", err));
}, []);


  const handleClearCart = () => {
    localStorage.removeItem("cart");
    setCartItems([]);
  };


  const handleSearch = () => {
    window.location.href = "/search";
  };

  return (
    <div className="cart-container">
      <header className="navbar">
        <button className="account" onClick={() => window.location.href="/seller"}>Account</button>

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

        <h1>Your Shopping Cart</h1>
      </header>

      <main className="content">
        {cartItems.length === 0 ? (
          <p>Your cart is empty.</p>
        ) : (
        <ul>
          {cartItems.map(order => (
            <li key={order[0]}>
              Order #{order[0]} — Item {order[3]} — Total: ${order[4]}
            </li>
          ))}
        </ul>

        )}
        <button onClick={handleClearCart}>Clear Cart</button>
      </main>
    </div>
  );
}
