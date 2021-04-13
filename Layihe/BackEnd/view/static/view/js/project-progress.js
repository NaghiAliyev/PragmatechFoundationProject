function run(barId,value){
    const myBar = document.getElementById(barId);
    const detail = document.getElementsByClassName('detail')
    let width = 0;
    let timeInt = setInterval(frame, 10);
    function frame() {
        if (width >= value) {
            clearInterval(timeInt);
        } else {
            if(value-10 <= width){

            }
            width+=1;
            
            myBar.style.width = width + '%'
        }
    }
}

run();