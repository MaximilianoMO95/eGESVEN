import React, { useState } from 'react';
import LoginCSS from './Login.module.css'; 

function Login() {
  const [isActive, setIsActive] = useState(false);

  const handleRegisterClick = () => {
    setIsActive(true);
  };

  const handleLoginClick = () => {
    setIsActive(false);
  };

  return (
    <div className={`${LoginCSS.container} ${isActive ? LoginCSS.active : ''}`}>
      <span className={LoginCSS.close}>
        <i className="bx bx-x"></i>
      </span>
      <div className={`${LoginCSS.formBox} ${LoginCSS.login}`}>
        <h2>Login</h2>
        <form action="">
          <div className={LoginCSS.inputBox}>
            <input type="text" name="username" id="username" placeholder="Username" />
            <i className="bx bxs-user"></i>
          </div>
          <div className={LoginCSS.inputBox}>
            <input type="password" name="password" id="password" placeholder="Password"/>
            <i className="bx bxs-lock"></i>
          </div>
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
