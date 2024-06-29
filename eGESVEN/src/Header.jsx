
function Header() {
    return(
        <header>
            <h2>eGESVEN</h2>
            <nav className="navBar">
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Productos</a>
                <a href="#">Carrito</a>
                <button className="btn" type="submit">Login</button>
            </nav>
        </header>
    );
}

export default Header