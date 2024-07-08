import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import SlidesCSS from './Slides.module.css';
import calafateImage from '../assets/calafate.jpg';
import jackImage from '../assets/jack-daniels.jpg';
import johnieImage from '../assets/Jw.jpg';
import kunstImage from '../assets/Kunst.jpg';
import vodkaImage from '../assets/Vodka.jpg';

const productImages = {
  'calafate.jpg': calafateImage,
  'jack-daniels.jpg': jackImage,
  'jw.jpg': johnieImage,
  'kunst.jpg': kunstImage,
  'vodka.jpg': vodkaImage,
};

function Arrow(props) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, display: "block", background: "black" }}
      onClick={onClick}
    />
  );
}

function Slides() {
  const [productData, setProductData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch data from the API
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/products/');
        if (!response.ok) {
          throw new Error('Failed to fetch products');
        }
        const data = await response.json();
        setProductData(data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 2,
    nextArrow: <Arrow />,
    prevArrow: <Arrow />,
    initialSlide: 0,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 2
        }
      },
    ]
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className={SlidesCSS.container}>
      <Slider {...settings}>
        {productData.map((product) => (
          <div key={product.id} className={SlidesCSS.cards}>
            <img src={productImages["jack-daniels.jpg"]} alt={`Imagen ${product.name}`} className={SlidesCSS.cardsImg} />
            <div className={SlidesCSS.cardsBody}>
              <h3 className={SlidesCSS.cardsTitle}>{product.name}</h3>
              <p className={SlidesCSS.cardsPrice}>{`$ ${product.price} CPL`}</p>
              <button className={SlidesCSS.cardsBtn}>Comprar</button>
            </div>
          </div>
        ))}
      </Slider>
    </div>
  );
}

export default Slides;
