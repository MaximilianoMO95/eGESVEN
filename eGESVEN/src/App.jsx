import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { useEffect } from 'react';
import Home from "./pages/Home";
import Productos from "./pages/Productos";
import Basket from "./pages/Basket";
import './index.css';

function App() {
  const location = useLocation();

  useEffect(() => {
    if (location.pathname === '/Productos') {
      document.body.classList.add('body-block');
      document.body.classList.remove('body-flex');
    } else {
      document.body.classList.add('body-flex');
      document.body.classList.remove('body-block');
    }
  }, [location.pathname]);

  return (
    <div>
      <Routes>
        <Route index element={<Home />} />
        <Route path='/home' element={<Home />} />
        <Route path='/productos' element={<Productos />} />
        <Route path='/Basket' element={<Basket />} />
      </Routes>
    </div>
  );
}

function AppWrapper() {
  return (
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
}

export default AppWrapper;
