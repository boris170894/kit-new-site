document.addEventListener('DOMContentLoaded', () => {
    const line = document.querySelector('.draw')
    const history__datas = document.querySelectorAll('.history__data')
    const history__contents = document.querySelectorAll('.history__content')


    for (let i = 0; i < history__datas.length; i++) {
        if (i > 2) {
            history__datas[i].style.marginLeft = '-10%'  
            history__contents[i].style.marginLeft = '-10%'  
        }
    }

    window.addEventListener('scroll', (e) => {
        let scrollPosition = window.scrollY;
    
        // Высота контента минус высота окна браузера
        let contentHeight = document.querySelector('.page__histories').offsetHeight;
        let windowHeight = window.innerHeight;
        
        if (window.innerWidth <= 600 || window.innerWidth >= 1050) {
            if (scrollPosition > windowHeight / 10 &&  scrollPosition < contentHeight) {
                let scaleHeight = (scrollPosition /  (contentHeight - 300) * 100)

                for (let i = 0; i < history__datas.length; i++) {
                    if (scaleHeight > i * 6) {
                        history__datas[i].style.margin = 0
                        history__contents[i].style.margin = 0
                    }
                    
                }

                line.style.height = scaleHeight + '%';
            }
        } else {
            if (scrollPosition > windowHeight / 10 &&  scrollPosition < contentHeight) {
                let scaleHeight = (scrollPosition /  (contentHeight - 300) * 115)

                for (let i = 0; i < history__datas.length; i++) {
                    if (scaleHeight > i * 6) {
                        history__datas[i].style.margin = 0
                        history__contents[i].style.margin = 0
                    }
                    
                }

                line.style.height = scaleHeight + '%';
            }
        }
    });
})