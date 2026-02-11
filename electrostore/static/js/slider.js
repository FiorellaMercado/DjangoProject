document.addEventListener("DOMContentLoaded", function() {
  let currentSlide = 0;
  const slides = document.querySelectorAll('.slider-image');
  const pagination = document.querySelector('.slider-pagination');
  const prevButton = document.querySelector('.prev-button');
  const nextButton = document.querySelector('.next-button');

  // Crear los indicadores de paginación
  slides.forEach((_, i) => {
    const indicator = document.createElement('span');
    indicator.classList.add('pagination-item');
    indicator.addEventListener('click', () => showSlide(i));
    pagination.appendChild(indicator);
  });

  function showSlide(index) {
    slides.forEach((slide, i) => {
      if (i === index) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });
    updatePagination(index);
  }

  function updatePagination(index) {
    const paginationItems = pagination.querySelectorAll('.pagination-item');
    paginationItems.forEach((item, i) => {
      if (i === index) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }

  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  }

  // Mostrar la primera imagen al cargar la página
  showSlide(currentSlide);

  // Cambiar la imagen cada 5 segundos
  setInterval(nextSlide, 5000);

  prevButton.addEventListener('click', function() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  });

  nextButton.addEventListener('click', function() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  });
});