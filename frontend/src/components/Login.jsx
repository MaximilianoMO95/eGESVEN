import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import LoginCSS from './Login.module.css';
import { useAuth } from '../context/AuthContext';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const { authState, login } = useAuth();
  const navigate = useNavigate();

  const [isActive, setIsActive] = useState(false);

  const handleRegisterClick = () => {
    setIsActive(true);
  };

  const handleLoginClick = () => {
    setIsActive(false);
  };

  useEffect(() => {
    if (authState.isAuthenticated) {
      navigate('/Productos');
    }
  }, [authState.isAuthenticated, navigate]);

  const handleLoginSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/v1/login/access-token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          username: username,
          password: password,
        }),
      });

      if (!response.ok) {
        throw new Error('Login failed. Please check your credentials.');
      }

      const data = await response.json();
      login(data.access_token, username);
      setSuccessMessage('Login successful!');
      setErrorMessage('');
      navigate('/Productos');
    } catch (error) {
      setErrorMessage(error.message);
      setSuccessMessage('');
    }
  };

  return (
    <div className={`${LoginCSS.container} ${isActive ? LoginCSS.active : ''}`}>
      <div className={`${LoginCSS.formBox} ${LoginCSS.login}`}>
        <h2>Login</h2>
        <form onSubmit={handleLoginSubmit}>
          <div className={LoginCSS.inputBox}>
            <input
              type="text"
              name="username"
              id="username"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <i className="bx bxs-user"></i>
          </div>
          <div className={LoginCSS.inputBox}>
            <input
              type="password"
              name="password"
              id="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <i className="bx bxs-lock"></i>
          </div>
          {errorMessage && <p className={LoginCSS.error}>{errorMessage}</p>}
          {successMessage && <p className={LoginCSS.success}>{successMessage}</p>}
          <div className={LoginCSS.noAccount}>
            <p>No tienes cuenta? <a href="#" className={LoginCSS.registerLink} onClick={handleRegisterClick}>Registrate</a></p>
          </div>
          <button className={LoginCSS.btnLogin} type="submit">Login</button>
        </form>
      </div>

      <div className={`${LoginCSS.formBox} ${LoginCSS.register}`}>
        <h2>Registro</h2>
        <form action="">
          <div className={LoginCSS.inputBox}>
            <input type="text" name="username" id="username" placeholder="Username" />
            <i className="bx bxs-user"></i>
          </div>
          <div className={LoginCSS.inputBox}>
            <input type="email" name="email" id="email" placeholder="Email" />
            <i className="bx bxs-envelope"></i>
          </div>
          <div className={LoginCSS.inputBox}>
            <input type="password" name="password" id="password" placeholder="Password"/>
            <i className="bx bxs-lock-alt"></i>
          </div>
          <div className={LoginCSS.noAccount}>
            <p>Ya tienes cuenta? <a href="#" className={LoginCSS.loginLink} onClick={handleLoginClick}>Login</a></p>
          </div>
          <button className={LoginCSS.btnLogin} type="submit">Registro</button>
        </form>
      </div>
    </div>
    
  );
}

export default Login;
