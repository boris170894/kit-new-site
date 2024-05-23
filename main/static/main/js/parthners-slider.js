const parthners = document.querySelectorAll('.page__achivement')
const parthners_collection = document.querySelector('.page__archievements__collection')

const parthnerButonLeft = document.querySelector('.page__archivements__left')
const parthnerButonRight = document.querySelector('.page__archivements__right')

let numbers

if (parthners.length > 4 && window.innerWidth > 600) {
    numbers = [0,1,2,3]
} else if (parthners.length > 2 && window.innerWidth <= 600) {
    numbers = [1,2]
} else {
    parthnerButonLeft.style.opacity = 0
    parthnerButonRight.style.opacity = 0

    for (let i = 0; i < parthners.length; i++) {
        numbers.push(i)
    }
}

// TODO: Base rendering
renderParthners(numbers)

// TODO: If you click on the left button
parthnerButonLeft.onclick = () => {
    if (numbers[0] == 0) {
        numbers.unshift(parthners.length-1)
        numbers.pop()
    } else {
        numbers.unshift(numbers[0]-1)
        numbers.pop()
    }
    renderParthners(numbers)
}

// TODO: If you click on the right button
parthnerButonRight.onclick = () => {
    if (numbers[numbers.length -1 ] == parthners.length-1) {
        numbers.push(0)
        numbers.shift()
    } else {
        numbers.push(numbers[numbers.length-1]+1)
        numbers.shift()
    }
    renderParthners(numbers)
}

// TODO: render content function
function renderParthners(numbers) {
    parthners_collection.innerHTML = ''

    for (const number of numbers) {
        let parthner = parthners[number]
    
        let parthnerImg = parthner.querySelector('img').getAttribute('src')
        let parthnerHref = parthner.querySelector('a').getAttribute('href')
        let parthnerText = parthner.querySelector('a').innerText

        parthners_collection.innerHTML += `
            <div class="page__achivement">
                <img src="${parthnerImg}" alt="${parthnerText}">
                <a href="${parthnerHref}" target="_blank">${parthnerText}</a>
            </div>   
        `
    }
}