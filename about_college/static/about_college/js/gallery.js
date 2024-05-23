const images = document.querySelectorAll('.page__image')
const galleryWindow = document.querySelector('#GalleryWindow')
const galleryWindowContent = document.querySelector('#GalleryWindowContent')

const closeWindow = document.querySelector('#GalleryWindowClose')
const galleryWindowTitle = document.querySelector('#GalleryWindowTitle')
const galleryWindowImage = document.querySelector('#GalleryWindowImage')

const prevImage = document.querySelector('#PrevImage')
const nextImage = document.querySelector('#NextImage')

const allImages = document.querySelectorAll('.page__image')
const allSlides = []
let globalIndex = 0

for (const image of allImages) {
    let img = image.querySelector('img').src
    let title = image.querySelector('h3').textContent

    allSlides.push({
        title: title,
        src: img,
    })
}

const leftSliderImage = () => {
    globalIndex - 1 != -1 ? globalIndex-- : globalIndex = allSlides.length - 1
}

 const rightSliderImage = () => {
    globalIndex + 1 != allSlides.length  ? globalIndex++ : globalIndex = 0
}

const renderSlide = () => {
    galleryWindowTitle.style.opacity = 0;
    galleryWindowImage.style.opacity = 0;

    let slide = allSlides[globalIndex]
    console.log(globalIndex)
    console.log(slide)

    setTimeout(() => {
        galleryWindowTitle.innerHTML = slide['title']
        galleryWindowImage.src = slide['src']

        setTimeout(() => {
            galleryWindowTitle.style.opacity = 1;
            galleryWindowImage.style.opacity = 1;
        }, 200)
    }, 200)
}

const DisplayOpacityChange = (w, display, opacity, title, image) => {
    if (image) {
        globalIndex = allSlides.findIndex(slide => slide.title === title && slide.src === image);

        renderSlide()
    }

    w.style.display = display

    setTimeout(() => {
        w.style.opacity = opacity
    }, 300)
}

closeWindow.addEventListener('click', (e) => {
    DisplayOpacityChange(galleryWindow, 'none', 0)
})

document.addEventListener('keydown', (e) => {
    if (e.key == 'Escape') {
        DisplayOpacityChange(galleryWindow, 'none', 0)
    }
})


images.forEach((image) => {
    image.addEventListener('click', (e) => {
        let img = image.querySelector('img').src
        let title = image.querySelector('h3').textContent

        DisplayOpacityChange(galleryWindow, 'flex', 1, title, img)
    })
})

prevImage.addEventListener('click', (e) => {
    leftSliderImage()
    renderSlide()
})

nextImage.addEventListener('click', (e) => {
    rightSliderImage()
    renderSlide()
})