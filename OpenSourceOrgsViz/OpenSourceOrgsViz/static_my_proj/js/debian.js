// creating element of debian image
var debian = document.getElementById("debian");


debian.style.width="90px";
debian.style.left="300px";
debian.style.top="100px";

// Image can be placed anywhere in the website so change position to aboslute
debian.style.position="absolute";

var boundX=window.innerWidth;
var boundY=window.innerHeight;

var speed = 5;
var x = 1;
var y = 1;

function Debian() {
    // coordinates of image element
    var posX = debian.offsetLeft;
    var posY = debian.offsetTop;

    if(posX + debian.offsetWidth > boundX || posX < 0){
        x *= -1;
    }

    if(posY + debian.offsetHeight > boundY || posY < 0){
        y *= -1;
    }

    // increase x,y position of element
    debian.style.left = debian.x + (speed*x) + "px";
    debian.style.top = debian.y + (speed*y) + "px";


    setTimeout(Debian, 100);
}

Debian();
