const nextIcon = '<i class="fas fa-angle-right">'
const prevIcon = '<i class="fas fa-angle-left">'
$(function(){
    $('.owl-carousel').owlCarousel({
        margin:30,
        dots: false,
        nav: true,
        // loop:true,
        navText: [prevIcon, nextIcon],
        // autoplay: false,
        // autoplayTimeout: 3500,
        // autoplayHoverPause: false,
        responsive: {
            0 : { items : 1},
            750 : { items : 2},
            1170 : { items : 3},
            1250 :{items : 4}
        }
    });
});