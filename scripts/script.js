function random_color() {
    var x = Math.floor(Math.random() * 256);
    var y = Math.floor(Math.random() * 256);
    var z = Math.floor(Math.random() * 256);
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
    document.body.style.backgroundColor = bgColor
//    document.html.style.background = bgColor;
    }
function reset_color(){
  document.body.style.backgroundColor = "#ffb5b5"
}
