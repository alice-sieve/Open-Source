// creating element of debian image
var ubuntu = document.getElementById("ubuntu");

ubuntu.style.width="70px";
ubuntu.style.left="50px";
ubuntu.style.top="50px";

// Image can be placed anywhere in the website so change position to aboslute
ubuntu.style.position="absolute";

var boundX=window.innerWidth;
var boundY=window.innerHeight;

var speed = 5;
var x = 1;
var y = 1;

function Ubuntu() {
     
    // coordinates of image element
    var posX = ubuntu.offsetLeft;
    var posY = ubuntu.offsetTop;

    if(posX + ubuntu.offsetWidth > boundX || posX < 0){
        x *= -1;
    }
    
    if(posY + ubuntu.offsetHeight > boundY || posY < 0){
        y *= -1;
    }

    // increase x,y position of element
    ubuntu.style.left = ubuntu.x + (speed*x) + "px";
    ubuntu.style.top = ubuntu.y + (speed*y) + "px";


    setTimeout(Ubuntu, 100);
}

Ubuntu();
