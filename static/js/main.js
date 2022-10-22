function backgroundcanvas(mouseX, mouseY) {
    const canvas = document.getElementById("canvas");
    canvas.width = window.innerWidth; // mettre à la taille de la fenêtre
    canvas.height = window.innerHeight;
    var bounds = canvas.getBoundingClientRect();
    mouseX = mouseX - bounds.left; // corriger la position de la souris par rapport aux bords
    mouseY = mouseY - bounds.top;
    let space = 45; // espacement entre les points
    const ctx = canvas.getContext("2d");
    for (let x = 0; x<canvas.width; x+=space) {
        for (let y = 0; y<canvas.height; y+=space) {
            let distance = Math.sqrt((mouseX-x)**2 + (mouseY-y)**2);
            if (distance > 100) {
                ctx.beginPath();
                ctx.arc(x, y, 1, 0, 2 * Math.PI, true); // ontrace les pints (cercle)
                ctx.stroke();
            }
            else if (distance < 20) {
                continue
            }
            else {
                if (x - mouseX > 0) {
                    newx = x + (mouseX/distance);
                }
                if (x - mouseX < 0) {
                    newx = x - (mouseX/distance);
                }
                if (y - mouseY > 0) {
                    newy = y + (mouseY/distance);
                }
                if (y - mouseY < 0) {
                    newy = y - (mouseY/distance);
                }
                ctx.beginPath();
                ctx.arc(newx, newy, 1, 0, 2 * Math.PI, true); // ontrace les pints (cercle)
                ctx.stroke();
            }
        }
    }
}


window.addEventListener("DOMContentLoaded", function(){ // on attend que le DOM se charge
    document.addEventListener('mousemove', (event) => {
        backgroundcanvas(event.clientX, event.clientY);
        //console.log(`Mouse X: ${event.clientX}, Mouse Y: ${event.clientY}`);
    });
});