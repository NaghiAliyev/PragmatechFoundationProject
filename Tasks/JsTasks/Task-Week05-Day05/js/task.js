let images=['img/1.jfif','img/2.jpg','img/3.jfif','img/4.jfif'];
let informationTexts=[
    "Walter White. He is chemistry teacher and genius man.",
    "Skylar White. Walter's wife, she is inconsiderate and stupid.",
    "Mike Ehrmantraut, He's assassin and he is the best of his job.",
    "Jesse Pinkman. He is Walter's student and he is emotional."
]
let navigationDots= document.querySelector('.navigation-dots');
let slide=document.querySelector('.slide');
let count;    
function nextSlide(){
    count++;
    if(count==images.length){
        count=0;
    }
    console.log('count = ' + count + ' ' + images[count])
    slide.setAttribute('src',images[count]);
    setText(count);
    setActiveSlide(count);
}
function previousSlide(){
    count--;
    if(count<0){
        count=images.length-1;
    }
    console.log('count = ' + count + ' ' + images[count])
    slide.setAttribute('src',images[count]);
    setText(count);
    setActiveSlide(count);
}
function setText(index){
    let paragraph=document.querySelector('.about');
    paragraph.innerHTML=informationTexts[index];
}
(function(){
    // let max=4;
    // let min=0;
    // randomIndex=Math.floor(Math.random() * (max - min)) + min;
    randomIndex=Math.floor(Math.random() * 4);
    count=randomIndex;
    slide.setAttribute('src',images[randomIndex]);
    setText(randomIndex);
    setActiveSlide(randomIndex);
    setInterval(nextSlide, 3500);
})()
function setActiveSlide(index){
    let currentActive = document.querySelector('.single-dot.active');
    currentActive.classList.remove('active');
    navigationDots.children[index].classList.add('active');
}
function goToThis(element){
    let forAmount;
    if(element.id>count){
        forAmount=element.id-count;
        for(i=0;forAmount>i;i++){
            nextSlide();
        }
    }
    else if(element.id < count){
        forAmount=count-element.id;
        for(i=0;forAmount>i;i++){
            previousSlide();
        }
    }
    
    console.log(forAmount);
}
