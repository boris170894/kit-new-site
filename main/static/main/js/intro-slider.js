const images = [
    'intro6.jpg',
    'intro3.jpg',
    'intro1.jpg',
    'intro5.jpg',
]
let base_i = 0

const intro__image = document.querySelector('.intro__image')
const intro__menu = document.querySelector('.intro__menu')

// Добавление в меню колличество опций выбора для переключения фото
for (let i = 0; i < images.length; i++) {
    const opt = document.createElement('div')

    opt.classList.add('intro__menu__option')
    i == 0 ? opt.classList.add('active') : ''

    opt.innerHTML = '<span></span>'

    intro__menu.appendChild(opt)
}

const changeImage = (i) => {
    intro__image.style.opacity = 0
        setTimeout(() => {
            intro__image.style.backgroundImage = `url('/static/main/img/intro/${images[i]}')`
            setTimeout(() => {
                intro__image.style.opacity = 1
            }, 300)
        }, 300)
        intro__menu__options.forEach(opt => {
            opt.classList.remove('active')
        })

        intro__menu__options[i].classList.add('active')
}

const intro__menu__options = document.querySelectorAll('.intro__menu__option')

// При клике на разные опции менять изображение на фото
for (let i = 0; i < intro__menu__options.length; i++) {
    intro__menu__options[i].addEventListener('click', () => {
        changeImage(i)  
    })
}
 
setInterval(() => {
    if (base_i+1 == intro__menu__options.length) {
        base_i = 0
        changeImage(base_i)
    } else {
        changeImage(++base_i)
    }
}, 5000)