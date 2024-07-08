import HeaderCSS from './Header.module.css'; 

function Header() {
    return(
        <header className={HeaderCSS.header}>
            <h2>eGESVEN</h2>
            <nav className={HeaderCSS.navBar}>
                <a href="../Home">Home</a>
                <a href="#">About</a>
                <a href="../Productos">Productos</a>
                <a href="../Basket">Carrito</a>
                <button className={HeaderCSS.btn} type="submit">Login</button>
            </nav>
        </header>
    );
}

export default Header