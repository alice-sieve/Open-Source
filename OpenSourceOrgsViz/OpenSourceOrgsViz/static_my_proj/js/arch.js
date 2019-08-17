// creating element of arch image
var arch = document.getElementById("arch");


arch.style.width="80px";
arch.style.left="150px";
arch.style.top="150px";

// Image can be placed anywhere in the website so change position to aboslute
arch.style.position="absolute";

var boundX=window.innerWidth;
var boundY=window.innerHeight;

var speed = 5;
var x = 1;
var y = 1;

function Arch() {
    // coordinates of image element
    var posX = arch.offsetLeft;
    var posY = arch.offsetTop;

    if(posX + arch.offsetWidth > boundX || posX < 0){
        x *= -1;
    }

    if(posY + arch.offsetHeight > boundY || posY < 0){
        y *= -1;
    }

    // increase x,y position of element
    arch.style.left = arch.x + (speed*x) + "px";
    arch.style.top = arch.y + (speed*y) + "px";


    setTimeout(Arch, 100);
}

Arch();
