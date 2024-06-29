
function Login() {
    return(
        <div className="container">
            <span className="close">
            <i class='bx bx-x' ></i>
            </span>
            <h2>Login</h2>
            <form action="">
                <div className="input-box">
                    <input type="text" name="username" id="username" placeholder="Username" />
                    <i class='bx bxs-user'></i>
                </div>
                <div className="input-box">
                    <input type="password" name="username" id="username" placeholder="Password"/>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <div className="register">
                    <p>No tienes cuenta? <a href="">Registrate</a></p>
                </div>
                <button className="btn-login" type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login