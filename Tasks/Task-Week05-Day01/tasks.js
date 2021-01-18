ededler=[1,3,4,6,4,1,101,99]

function topla(){
    cem=0;
    for(i=0;i<ededler.length;i++){
        cem += ededler[i];
    }
    console.log(cem);
}
// topla();

function cutleriTopla(){
    cem=0;
    for(i=0;i<ededler.length;i++){
        if(ededler[i]%2==0){
            cem += ededler[i];
        }
    }
    console.log(cem);
}

// cutleriTopla();

function tekleriTopla(){
    cem=0;
    for(i=0;i<ededler.length;i++){
        if(ededler[i]%2==1){
            cem += ededler[i];
        }
    }
    console.log(cem);
}

// tekleriTopla();

function tekrarlananlarinSayi(){
    console.log(ededler);
    tekrarSayi=0;
    for(i=0;i<ededler.length;i++){
        eded=ededler[i]
        say=0;
        for(j=i;j<ededler.length;j++){
            if(ededler[j]==eded){
                say++;
            }
        }
        if(say>1){
            tekrarSayi++;
        }
    }
    console.log(tekrarSayi);
}

// tekrarlananlarinSayi();

function ikireqemlileriTap(){
    say=0;
    for(i=0;i<ededler.length;i++){
        if(ededler[i]>9 && ededler[i]<100){
            say++;
        }
    }
    console.log(say);
}

// ikireqemlileriTap()

function azalanSiraylaYazdir(){
    ededlerinTekrari=ededler;
    siralanmisEdedler=[]
    for(j=0;j<ededlerinTekrari.length;j++){
        enBoyuk=ededlerinTekrari[0]
        enBoyukOlanIndex=0;
        for(i=0;i<ededlerinTekrari.length;i++){
            if(ededlerinTekrari[i]>enBoyuk){
                enBoyuk=ededlerinTekrari[i];
                enBoyukOlanIndex=i;
            }
        }
        siralanmisEdedler[j]=enBoyuk;
        ededlerinTekrari[enBoyukOlanIndex]=0;
    }
    
    console.log(siralanmisEdedler)
}

// azalanSiraylaYazdir();