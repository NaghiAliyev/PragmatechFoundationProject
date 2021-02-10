let slides = document.querySelector('.box-ch-contents').children;
let nextSlide = document.querySelector('.right-slide');
let prevSlide = document.querySelector('.left-slide');
let index = 0;
let totalSlides = slides.length;

function run(){
    const myBar = document.getElementById('myBar');
    let width = 0;
    let slower = 1;
    let timeInt = setInterval(frame, 50);

//  barın sona qədər dolmasında və dolduqdan sonra sıfıra enməsində problem var.

    function frame() {
        if (width >= 100) {
            clearInterval(timeInt);
            goTo('next');
            run();
            // timeInt = setInterval(frame, 50);

        } else {
            width+= slower;
            if(width >= 99 || width <= 1){
                slower=0.25;
            }else{
                slower=1;
            }
            myBar.style.width = width + '%'
        }
    }
}

run();

nextSlide.onclick = function(){
    goTo('next')
}

prevSlide.onclick = function(){
    goTo('prev')
}

function goTo (direction){
    if(direction == 'next'){
        index++;
        if(index == totalSlides){
            index=0;
        }
        for(let i=0; i<slides.length;i++){
            slides[i].classList.remove('active');
        }
        slides[index].classList.add('active')
    }else{
        index--;
        if(index == -1){
            index=totalSlides -1;
        }
        for(let i=0; i<slides.length;i++){
            slides[i].classList.remove('active');
        }
        slides[index].classList.add('active')
    }
}
