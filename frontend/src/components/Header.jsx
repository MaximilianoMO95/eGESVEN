import React from 'react';
import { useNavigate } from 'react-router-dom';

import { useAuth } from '../context/AuthContext';
import HeaderCSS from './Header.module.css';

function Header() {
  const { authState, logout } = useAuth();
  const navigate = useNavigate();

  const handleAuthClick = () => {
    if (authState.isAuthenticated) {
      logout();
    }

    navigate('/');
  };

  return (
    <header className={HeaderCSS.header}>
      <h2>eGESVEN</h2>
      <nav className={HeaderCSS.navBar}>
        <a href="../Home">Home</a>
        <a href="#">About</a>
        <a href="../Productos">Productos</a>
        <a href="../Basket">Carrito</a>
        <button className={HeaderCSS.btn} type="button" onClick={handleAuthClick}>
          {authState.isAuthenticated ? 'Logout' : 'Login'}
        </button>
      </nav>
    </header>
  );
}

export default Header;
