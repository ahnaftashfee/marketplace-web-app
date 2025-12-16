import React, { useState, useEffect } from "react";
import {useParams} from "react-router-dom";
import axios from "axios";
import "./base.css";
//jj
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";

export default function Product() {
    //const [form, setForm] = useState({ buyer_id: "", seller_id: "", item_id: "", total: ""})
    const [searchTerm, setSearchTerm] = useState("");
    const [product, setProduct] = useState(null);
    const { id } = useParams();


    const handleSearch = () => {
        window.location.href = "/search";
    };

    const fetchProduct = async () => {
        try {
            const res = await axios.get(`${API_BASE_URL}/api/item/${id}`);
            setProduct(res.data.item);
        } catch (error) {
            console.error("Error fetching product: ", error);
        }
    };

    const handleAddToCart = async () => {
    if (!product) return;

    const buyer_id = localStorage.getItem("seller_id"); // logged-in user
    const seller_id = product.seller_id;                // from product data
    const item_id = product.id;                        // product ID
    const total = product.price;                       // product price

    try {
        const res = await axios.post(`${API_BASE_URL}/api/add_order`, {
            buyer_id,
            seller_id,
            item_id,
            total
        });

        alert("Item added to cart!");
    } catch (error) {
        console.error("Error adding order:", error);
        alert("Could not add item to cart.");
    }
};


    useEffect(() => {
        fetchProduct();
    }, [id]);

    return (
    <div className="home-container">
        <header className="navbar">
        <button className="account" onClick={() => window.location.href="/seller"}>Account</button>
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

        <main className="product"> 
            {product ? (
                <>
                <h2 className="Product-title" >{product.title}</h2>
                <h2 className="Product-seller">{product.seller_username}</h2>
                <h3 className="description">{product.description}</h3>
                <button className="add-to-cart-btn" onClick={handleAddToCart}>Add to Cart</button>
                </>
            ) : (
                <p>Loading...</p>
            )}

        </main>

    </div>
    );
}