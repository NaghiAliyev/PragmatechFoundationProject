(function(){
    let main=document.getElementsByTagName('body')[0];
    let section=document.createElement('section');
    section.setAttribute('id','gallery')

    let container=document.createElement('div');
    container.setAttribute('class','container');
    let imgCount=1;
    for(i=0;i<2;i++){
        let row=document.createElement('div');
        row.setAttribute('class','row')
        for(j=0;j<3;j++){
            let col4=document.createElement('div');
            col4.setAttribute('class','col-4')

            let box=document.createElement('div');
            box.setAttribute('class','box');
            col4.appendChild(box);

            let image=document.createElement('img');
            let path='img/'+(imgCount++)+'.jpg';
            image.setAttribute('src',path);
            imgRegulator(image);
            box.appendChild(image)

            row.appendChild(col4);
        }        
        container.appendChild(row);
    }
    section.appendChild(container);
    main.appendChild(section);
})()

function imgRegulator(image){
    image.style.width="100%";
    image.style.height="100%";
    image.style.objectFit="cover";        
}
