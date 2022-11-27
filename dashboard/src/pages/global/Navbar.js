import React, { useState } from "react";
import "./Navbar.css";

import { NavLink as Link } from 'react-router-dom';



const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="Navbar">
      <Link className="nav-logo" to="/">AJSN Transport</Link>
      <div className={`nav-items ${isOpen && "open"}`}>
        <Link onClick={() => setIsOpen(!isOpen)} to="/">Home</Link>
        <Link onClick={() => setIsOpen(!isOpen)} to="/bookings">Bookings</Link>
        <Link onClick={() => setIsOpen(!isOpen)} to="/drivers">Drivers</Link>
        <Link onClick={() => setIsOpen(!isOpen)} to="/team">Team</Link>
        {/* <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/service">Service</a>
        <a href="/contact">Contact</a> */}
      </div>
      <div
        className={`nav-toggle ${isOpen && "open"}`}
        onClick={() => setIsOpen(!isOpen)}
      >
        <div className="bar"></div>
      </div>
    </div>
  );
};

export default Navbar;