import React from "react";
import BasketCSS from "./Basket.module.css";

function BasketC({ basketItems, onRemoveItem }) {
  return (
    <div className={BasketCSS.container}>
      <h2 className={BasketCSS.title}></h2>
      {basketItems.length === 0 ? (
        <p className={BasketCSS.empty}>Tu carrito esta vacio</p>
      ) : (
        <ul className={BasketCSS.items}>
          {basketItems.map((item) => (
            <li key={item.id} className={BasketCSS.item}>
              <img src={item.image} alt={item.name} className={BasketCSS.itemImg} />
              <div className={BasketCSS.itemDetails}>
                <h3 className={BasketCSS.itemTitle}>{item.name}</h3>
                <p className={BasketCSS.itemPrice}>${item.price}</p>
                <button onClick={() => onRemoveItem(item.id)} className={BasketCSS.itemBtn}>Remove</button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default BasketC;
