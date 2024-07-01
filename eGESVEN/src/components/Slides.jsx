import React, {useState, useEffect} from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import SlidesCSS from './Slides.module.css';
import calafateImage from '../assets/calafate.jpg';
import jackImage from '../assets/jack-daniels.jpg'
import johnieImage from '../assets/Jw.jpg'
import kunstImage from '../assets/Kunst.jpg'
import vodkaImage from '../assets/Vodka.jpg'
import products from '../tests/mocks/products.json';

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
      style={{ ...style, display: "block", background: "black", }}
      onClick={onClick}
    />
  );
}

function Slides() {
  const [productData, setProductData] = useState([]);

  useEffect(() => {
    // Simulating fetching data from a JSON file for now
    setProductData(products.products);
  }, []);

  var settings = {
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

  return (
    <div className={SlidesCSS.container}>
      <Slider {...settings}>
        {productData.map((product) => (
          <div key={product.id} className={SlidesCSS.cards}>
            <img src={productImages[product.image_url]} alt={`Imagen ${product.name}`} className={SlidesCSS.cardsImg} />
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
