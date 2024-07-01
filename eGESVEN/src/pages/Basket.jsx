import React, { useState } from "react";
import Header from "../components/Header";
import BasketC from "../components/Basket";

import calafateImage from '../assets/calafate.jpg';
import jackImage from '../assets/jack-daniels.jpg'
import johnieImage from '../assets/Jw.jpg'
import kunstImage from '../assets/Kunst.jpg'
import vodkaImage from '../assets/Vodka.jpg'

const productImages = {
  'calafate.jpg': calafateImage,
  'jack-daniels.jpg': jackImage,
  'jw.jpg': johnieImage,
  'kunst.jpg': kunstImage,
  'vodka.jpg': vodkaImage,
};

function Basket() {
  const initialBasketItems = [
    {
      id: 1,
      name: "Cerveza Austral Calafate",
      price: 12.99,
      image: 'calafate.jpg',
    },
    {
      id: 2,
      name: "Jack Daniel's",
      price: 29.99,
      image: 'jack-daniels.jpg',
    },
    {
      id: 3,
      name: "Johnnie Walker",
      price: 35.00,
      image: 'jw.jpg',
    },
  ];

  const [basketItems, setBasketItems] = useState(
    initialBasketItems.map(item => ({ ...item, image: productImages[item.image] }))
  );

  const handleRemoveItem = (id) => {
    setBasketItems(basketItems.filter(item => item.id !== id));
  };

  return(
    <>
      <Header />
      <main>
        <h1>My Basket</h1>
        <BasketC basketItems={basketItems} onRemoveItem={handleRemoveItem} />
      </main>
    </>
  );
}

export default Basket
