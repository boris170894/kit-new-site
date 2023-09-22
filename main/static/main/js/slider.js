const page__about__slide = document.querySelector('.page__about__slide')

// places
const page__about__left__name = document.querySelector('#page__about__left__name')
const page__about__left__img  = document.querySelector('#page__about__left__img')
const page__about__right = document.querySelector('.page__about__right')

// buttons
const button__left = document.querySelector('.page__about__button__left')
const button__right = document.querySelector('.page__about__button__right')


let count = 0;

// TODO: ADD NEW SLIDER 
const materials = [
    {
        id: 1, 
        number: 45, 
        text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo animi unde blanditiis, exercitationem laudantium tempore qui culpa voluptas quo accusantium quod consequuntur delectus architecto? Optio eius maiores neque animi tenetur.',
        name: ['3d принтер picaso 3d', 'designer xl pro 2'],
        img: "/static/main/img/about/3d-printer-picaso-3d-designer-xl-pro-2.png"
    },
    {
        id: 2,
        number: 22,
        text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo animi unde blanditiis, exercitationem laudantium tempore qui culpa voluptas quo accusantium quod consequuntur delectus architecto? Optio eius maiores neque animi tenetur.',
        name: ['camera', ''],
        img: "/static/main/img/about/camera.png"
    },
    {
        id: 3,
        number: 12,
        text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo animi unde blanditiis, exercitationem laudantium tempore qui culpa voluptas quo accusantium quod consequuntur delectus architecto? Optio eius maiores neque animi tenetur.',
        name: ['cisco', ''],
        img: "/static/main/img/about/cisco.png"
    },
    {
        id: 4,
        number: 10,
        text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo animi unde blanditiis, exercitationem laudantium tempore qui culpa voluptas quo accusantium quod consequuntur delectus architecto? Optio eius maiores neque animi tenetur.',
        name: ['dji mavic', 'air 2s leaked 4'],
        img: "/static/main/img/about/dji-mavic-air-2s-leaked-4.png"
    },
]


// if you click on the left button
button__left.addEventListener('click', () => {
    console.log(materials[count])
    if (count-1 == -1) {
        count = materials.length - 1
    } else {
        count--
    }

    changeSlide(count)
})   

// if you click on the right button
button__right.addEventListener('click', () => {
    if (count+1 == materials.length) {
        count = 0
    } else {
        count++
    }

    changeSlide(count)
})
    

function changeSlide(count) {
    page__about__right.innerHTML = `
        <h2>${materials[count].number}</h2>
        <p>${materials[count].text}</p>
        <a href="">Поступить к нам 
            <span class="material-symbols-outlined">
            trending_flat
            </span>
        </a>
    `

    page__about__left__name.innerHTML = `
        <p>${materials[count].name[0]}</p>
        <p>${materials[count].name[1]}</p>
    `
    page__about__left__img.src = materials[count].img

    if (materials[count].img == '/static/main/img/about/camera.png')  {
        page__about__left__img.style.height = '100%'
    } else if (materials[count].img == '/static/main/img/about/cisco.png') {
        page__about__left__img.style.height = '100%'
    } else {
        page__about__left__img.style.height = '110%'
    }
}