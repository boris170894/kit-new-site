document.addEventListener("DOMContentLoaded", () => {
    const footer__up = document.querySelector('.footer__up')
    const navButton  = document.querySelector('.nav__menu')

    footer__up.style.display = 'none'
    footer__up.style.opacity = 0
    footer__up.style.bottom = 0

    if (window.innerWidth <= 1100) {
        navButton.style.backgroundColor = 'transparent'
    }

    window.addEventListener('scroll', (e) => {
        let scrollPosition = window.scrollY;
        let contentHeight = document.body.offsetHeight;
        let windowHeight = window.innerHeight;

        if (scrollPosition > windowHeight-200) {
            footer__up.style.display = 'flex'

            setTimeout(() => {
                footer__up.style.opacity = .4
                footer__up.style.bottom = '3.5vh'
            }, 300)
        } else {
            footer__up.style.opacity = 0
            footer__up.style.bottom = 0

            setTimeout(() => {
                footer__up.style.display = 'none'
            }, 300)
        }

        if (window.innerWidth <= 1100) {
            if (scrollPosition > windowHeight/2) {
                navButton.style.backgroundColor = 'white'
                navButton.style.boxShadow = '0 0 10px rgb(20,20,20,.2)'
            } else {
                navButton.style.backgroundColor = 'transparent'
                navButton.style.boxShadow = '0 0 10px rgb(20,20,20,.1)'
            }
        }
    
    })
})