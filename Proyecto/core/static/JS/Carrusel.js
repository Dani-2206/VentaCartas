var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    coverflowEffect: {
      depth: 300,
      spaceBetween: 10
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },
    breakpoints: {
      // Mostrar 2 diapositivas a la vez en dispositivos móviles
      640: {
        slidesPerView: 2
      }
    },
    pagination: {
      el: ".swiper-pagination",
      type: "bullets"
    },
    slidesPerView: 1, // Mostrar 2 diapositivas a la vez
    minslidesPerView: 1 // Mostrar al menos 1 diapositiva a la vez
})
var swiper = new Swiper(".mySwiper2", {
    slidesPerView: 1,
    spaceBetween: 50,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 1000, // Cambia cada 3 segundos
}})
