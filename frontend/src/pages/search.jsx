import React, { useState, useEffect } from "react";
import axios from "axios";
import "./base.css";
import "./search.css";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";
//jj
export default function SearchPage() {
  const [items, setItems] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  const seller_id = localStorage.getItem("seller_id");

  useEffect(() => {
    if (!seller_id) {
      alert("No seller logged in.");
      return;
    }
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const res = await axios.get(
        `${API_BASE_URL}/api/all_items`
      );
      console.log("Items:", res.data.items);
      setItems(res.data.items);
    } catch (error) {
      console.error("Error fetching seller items:", error);
    }
  };

  const filteredItems = items.filter(
    (item) =>
      item[2] && item[2].toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="search-container">
      <header className="navbar">
        <button className="account" onClick={() => window.location.href="/seller"}>Account</button>
        <h1 className="logo">Marketplace</h1>

        <div className="search-bar">
          <input
            type="text"
            className="search"
            placeholder="Search your items..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button className="search-btn">Search</button>
        </div>

        <a href="/cart" className="cart-btn">
          Open Cart
        </a>
      </header>

      <main className="content">
        <h2>Your Items</h2>

        {filteredItems.length === 0 ? (
          <p>No matching items found.</p>
        ) : (
          <ul className="item-list">
            {filteredItems.map((item) => (
              <li key={item[0]} className="item-card">
                <p className="item-title">
                  <b>{item[2]}</b>
                </p>
                <p className="item-desc">{item[3]}</p>
                <p className="item-price">Price: ${item[4]}</p>
                <button className="view-product" onClick={() => window.location.href=`/item/${item[0]}`}>View Product</button>
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
}
