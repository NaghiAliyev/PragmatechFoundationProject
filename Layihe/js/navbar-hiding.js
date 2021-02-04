/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".top-nav-bar").style.top = "0";
    if(currentScrollPos == 0)
        document.getElementById("navbar").style.top = "54px";
  } else {
    document.querySelector(".top-nav-bar").style.top = "-50px";
    document.getElementById("navbar").style.top = "0";
  }
  prevScrollpos = currentScrollPos;
}