// 55 years old
document.addEventListener('DOMContentLoaded', function () {
    const text = document.querySelector('#IntroID').value;
    const textContainer = document.getElementById('typing-text');
    let index = 0;
    let isDeleting = false;
  
    function typeText() {
      if (isDeleting) {
        textContainer.textContent = text.substring(0, index - 1);
        index--;
      } else {
        textContainer.textContent = text.substring(0, index + 1);
        index++;
      }
  
      if (index === text.length + 1) {
        isDeleting = true;
        setTimeout(typeText, 3000); // Задержка перед удалением текста
      } else if (index === 0) {
        isDeleting = false;
        setTimeout(typeText, 600); // Задержка перед началом печати текста
      } else {
        setTimeout(typeText, 150); // Задержка между символами
      }
    }
  
    typeText();
  });

// Slider logic  
document.addEventListener('DOMContentLoaded', () => {
    let slides = document.querySelectorAll('.page__about__slider')
    let nexti = document.querySelector('.nexti')
    let prev = document.querySelector('.prev')

    let slideNumber = 0

    // Скрытие всех сладов
    const hideSlides = () => {
        slides.forEach(slide => {
            slide.style.display = 'none'; 
        })
    }
    // Рендер слайда
    const RenderSlide = (n) => {
        hideSlides()

        changeOpacityStyle(slides[n])
        slides[n].style.display = 'flex';
    }

    // Добавление спец эффектов
    const changeOpacityStyle = (slide) => {
        let images = slide.querySelectorAll('img')
        let h2 = slide.querySelector('h2')
        let p = slide.querySelector('p')
        let title = slide.querySelector('.page__about__right__title')
        let link = slide.querySelector('a')

        let h2Length = h2.textContent.length;

        if (h2Length > 10) {
            h2.style.fontSize = '35px';
        } else if (h2Length > 20) {
            h2.style.fontSize = '30px';
        } else if (h2Length > 30) {
            h2.style.fontSize = '26px';
        }

        h2.style.opacity = 0 
        p.style.opacity = 0 
        title.style.opacity = 0
        link.style.opacity = 0

        setTimeout(() => {
            h2.style.opacity = 1
        }, 100)

        setTimeout(() => {
            p.style.opacity = 1
        }, 200)

        setTimeout(() => {
            title.style.opacity = 1
        }, 400)

        setTimeout(() => {
            link.style.opacity = 1
        }, 400)

        images.forEach((image, i) => {
            image.style.opacity = 0

            setTimeout(() => {
                image.style.opacity = 1
            }, 200 * i + 200)
        })
    }

    RenderSlide(0)

    prev.addEventListener('click', () => {
        if (slideNumber - 1 == -1 ) {
            slideNumber = slides.length - 1
        } else {
            slideNumber--
        }
        RenderSlide(slideNumber)
    })

    nexti.addEventListener('click' ,() => {
    })

    nexti.addEventListener('click', () => {
        if (slideNumber == slides.length - 1) {
            slideNumber = 0
        } else {
            slideNumber++
        }
        RenderSlide(slideNumber)
    })
})