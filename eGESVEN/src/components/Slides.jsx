import React from "react";
import Slider from "react-slick";
import calafateImage from '../assets/calafate.jpg';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import SlidesCSS from './Slides.module.css';

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
        <div className={SlidesCSS.cards}>
          <img src={calafateImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Título del Producto</h3>
            <p className={SlidesCSS.cardsPrice}>$XX.XX</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={calafateImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Título del Producto</h3>
            <p className={SlidesCSS.cardsPrice}>$XX.XX</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={calafateImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Título del Producto</h3>
            <p className={SlidesCSS.cardsPrice}>$XX.XX</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={calafateImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Título del Producto</h3>
            <p className={SlidesCSS.cardsPrice}>$XX.XX</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={calafateImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Título del Producto</h3>
            <p className={SlidesCSS.cardsPrice}>$XX.XX</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
      </Slider>
    </div>
  );
}

export default Slides;
