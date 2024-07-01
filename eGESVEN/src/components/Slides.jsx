import React from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import SlidesCSS from './Slides.module.css';
import calafateImage from '../assets/calafate.jpg';
import jackImage from '../assets/jack-daniels.jpg'
import johnieImage from '../assets/Jw.jpg'
import kunstImage from '../assets/Kunst.jpg'
import vodkaImage from '../assets/Vodka.jpg'

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
            <h3 className={SlidesCSS.cardsTitle}>Cerveza Austral</h3>
            <p className={SlidesCSS.cardsPrice}>$7.000</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={jackImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Jack Daniel's</h3>
            <p className={SlidesCSS.cardsPrice}>$21.000</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={johnieImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>JW Gold</h3>
            <p className={SlidesCSS.cardsPrice}>$40.000</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={kunstImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Kunstmann</h3>
            <p className={SlidesCSS.cardsPrice}>$6.900</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
        <div className={SlidesCSS.cards}>
          <img src={vodkaImage} alt="Imagen Cerveza Austral Calafate" className={SlidesCSS.cardsImg} />
          <div className={SlidesCSS.cardsBody}>
            <h3 className={SlidesCSS.cardsTitle}>Eristoff</h3>
            <p className={SlidesCSS.cardsPrice}>$5.000</p>
            <button className={SlidesCSS.cardsBtn}>Comprar</button>
          </div>
        </div>
      </Slider>
    </div>
  );
}

export default Slides;
