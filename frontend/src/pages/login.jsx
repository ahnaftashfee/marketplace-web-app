import React, { useState } from "react";
import axios from "axios";
import "./base.css";
//jj
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: ""});
  const [message, setMessage] = useState("");
  const [searchTerm, setSearchTerm] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${API_BASE_URL}/api/login`, form);

      setMessage(res.data.message);

   
      localStorage.setItem("seller_id", res.data.seller_id);

  
      window.location.href = "/seller";

    } catch (err) {
      setMessage("Server error. Please try again.");
      console.error(err);
    }
  };

  const handleCreateAccount = async () => {
    const username = prompt("Please enter the desired username:");
    const password = prompt("Please enter the desired password:");
    const seller_id = Math.floor(100000000 + Math.random() * 900000000);

    if (!username || !password) {
      alert("Username and password cannot be empty.");
      return;
    }

    try {
      const res = await axios.post(`${API_BASE_URL}/api/add_user`, {
        username: username,
        password: password,
        seller_id: seller_id
      });

      if (res.data.message) {
        setMessage("Account created successfully! You can now log in.");
      } else {
        setMessage("Account creation failed. Username may already exist.");
      }
    } catch (err) {
      console.error(err);
      setMessage("Server error. Please try again.");
    }
  };

  const handleSearch = () => {
    window.location.href = "/search";
  };

  return (
    <div className="home-container">
      <header className="navbar">
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
        <h2>Sign In or Create an Account to Continue</h2>

        <form className="login-form" onSubmit={handleLogin}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={form.username}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={form.password}
            onChange={handleChange}
            required
          />
          <button type="submit" className="login-btn">
            Log Back In
          </button>
        </form>

        <p className="msg">{message}</p>

        <button className="create-btn" onClick={handleCreateAccount}>
          Create an Account
        </button>
      </main>
    </div>
  );
}
