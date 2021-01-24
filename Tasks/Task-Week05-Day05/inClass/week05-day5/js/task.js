let container=document.querySelector('.container');
let images=['img/1.jpg','img/2.jpg','img/3.jpg','img/4.jpg','img/5.jpg','img/6.jpg','img/7.jpg','img/8.jpg']

colCount=3;
rowCount=Math.ceil(images.length/colCount)

let rowContent=''
let containerContent=''
let imageIndex=0;
for(let row=0;row<rowCount;row++){
    if((images.length%colCount != 0) && row == (rowCount-1)){
        console.log('row' + row);
        colCount=images.length%colCount;
    }
    for(let col=0;col<colCount;col++){

        let colContent=`
        <div class="col-4">
            <div class="box" onclick='showBigImage(this)'>
                <img src=${images[imageIndex]} alt="">
            </div>
        </div>
        `
        rowContent+=colContent
        imageIndex++
    }

    containerContent+=`
        <div class="row">
            ${rowContent}
        </div>
    `
    rowContent=''
}

container.innerHTML=containerContent

function showBigImage(element){
    overlayContent=`
    <div class="overlay" >
        <img src=${element.querySelector('img').getAttribute('src')} alt="">
        <div class="close"  onclick='closeImage(this)'>
            <i class="fas fa-times fa-2x xIcon"></i></div>
        </div>
    </div>
    `

    container.innerHTML=containerContent+overlayContent


}
function closeImage(element){
    document.getele
    container.removeChild(element.parentElement)
}