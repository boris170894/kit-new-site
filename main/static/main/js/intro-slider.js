const slider = document.querySelector(".slider");
const slides = document.querySelectorAll(".slide");
const intro__menu = document.querySelector('.intro__menu')
let currentIndex = 0;

for (let i = 0; i < slider.children.length; i++) {
    const div = document.createElement("div")

    div.classList.add('intro__menu__option')
    i == 0 ? div.classList.add('active') : ''

    div.innerHTML = '<span></span>'
    intro__menu.appendChild(div)
}

const intro__menu__options = document.querySelectorAll('.intro__menu__option')

function updateSlider(i) {
    const translateX = -i * 100;
    slider.style.transform = `translateX(${translateX}%)`;

    intro__menu__options.forEach(opt => {
        opt.classList.remove('active')
    })

    intro__menu__options[i].classList.add('active')
}

// При клике на разные опции менять изображение на фото
for (let i = 0; i < intro__menu__options.length; i++) {
    intro__menu__options[i].addEventListener('click', () => {
        updateSlider(i)  
    })
}


setInterval(() => {
    currentIndex++;
    if (currentIndex >= slider.children.length) {
        currentIndex = 0;
    }
    updateSlider(currentIndex);
}, 5000)