let slides = document.querySelector('.box-ch-contents').children;
let nextSlide = document.querySelector('.right-slide');
let prevSlide = document.querySelector('.left-slide');
let index = 0;
let totalSlides = slides.length;
const myBar = document.getElementById('myBar');
let wControl =false;
function run(){
    let width = 0;
    if(wControl){
        width=-20;
    }
    let timeInt = setInterval(frame, 100);
    
//  barın sona qədər dolmasında və dolduqdan sonra sıfıra enməsində problem var, qismən problem həll olundu.
    function frame() {
        if (width >= 105) {
            clearInterval(timeInt);
            myBar.style.display = "none";
            goTo('next');
            wControl=true;
            run();
        } else {
            if(width==0){
                myBar.style.display = "block";
            }
            width+=1;
            
            myBar.style.width = width + '%'
        }
    }
}

run();

nextSlide.onclick = function(){
    goTo('next');
}

prevSlide.onclick = function(){
    goTo('prev');
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
function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }