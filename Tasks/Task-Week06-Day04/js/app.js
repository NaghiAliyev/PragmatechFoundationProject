let textInput = `
    <div class="col-8 offset-2 my-2" onchange="myFunc()">
        <input type="text" class="form-control" id="meme-text-in" placeholder="mətni daxil edin" >
    </div>
`;

function addData(event){
    event.preventDefault();
    let contentText = `
    <div class="content-text "></div>
    `;
    let src = $('#url').val();

    let img =`
        <img src="${src}" alt="" class="meme-img" >
    `;

    document.querySelector('.meme-content').innerHTML= img + textInput + contentText;
}
function myFunc(){
    let textElement = document.createElement('div');
    let memeImg= document.querySelector('.meme-img');
    let imgWidth = memeImg.offsetWidth;
    let memeText = '';
    if($('#pos').val() == 'top'){
        memeText = `
            <div class="meme-text position-absolute bottom-0 start-0" style="top:0;width:${imgWidth + 'px'};">${$('#meme-text-in').val()}</div>
        `;
    }
    else{
        memeText = `
            <div class="meme-text position-absolute bottom-0 start-0" style="bottom:0;width:${imgWidth + 'px'};">${$('#meme-text-in').val()}</div>
        `;
    }
    // textElement.innerHTML=memeText;
    if(document.querySelector('.meme-text') != null){
        document.querySelector('.content-text').innerHTML = '';
    }
    document.querySelector('.content-text').innerHTML = memeText;
}