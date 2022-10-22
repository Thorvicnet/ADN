function backgroundcanvas(mouseX, mouseY) {
    const canvas = document.getElementById("canvas");
    canvas.width = window.innerWidth; // mettre à la taille de la fenêtre
    canvas.height = window.innerHeight;
    var bounds = canvas.getBoundingClientRect();
    mouseX = mouseX - bounds.left - scrollX; // corriger la position de la souris par rapport au scroll et bords
    mouseY = mouseY - bounds.top - scrollY;
    let space = 45; // espacement entre les points
    const ctx = canvas.getContext("2d");
    for (let x = 0; x<canvas.width; x+=space) {
        for (let y = 0; y<canvas.height; y+=space) {
            if (Math.sqrt((mouseX-x)**2 + (mouseY-y)**2) > 50) {
                ctx.beginPath();
                ctx.arc(x, y, 1, 0, 2 * Math.PI, true);
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