function backgroundcanvas(mouseX, mouseY) {
    const canvas = document.getElementById("canvas");
    canvas.width = window.innerWidth; // mettre à la taille de la fenêtre
    canvas.height = window.innerHeight;
    var bounds = canvas.getBoundingClientRect();
    mouseX = mouseX - bounds.left; // corriger la position de la souris par rapport aux bords
    mouseY = mouseY - bounds.top;
    let space = 45; // espacement entre les points default=45
    const ctx = canvas.getContext("2d");
    for (let x = 0; x<canvas.width; x+=space) {
        for (let y = 0; y<canvas.height; y+=space) {
            let distance = Math.sqrt((mouseX-x)**2 + (mouseY-y)**2);
            if (distance > 125) {
                ctx.beginPath();
                ctx.arc(x, y, 1, 0, 2 * Math.PI, true); // on trace les points (cercle) normalement
                ctx.stroke();
            }
            else if (distance < 20) { // les points partent trop loin après calcul (on les tracent pas)
                continue
            }
            else {
              let mov = (mouseX/distance)
              //let mov = (mouseX/((1)+Math.sqrt(distance**2))) // test de fonction différente
              if (x - mouseX > 0) { // pour les différentes directions
                  newx = x + mov;
              }
              if (x - mouseX < 0) {
                  newx = x - mov;
              }
              if (y - mouseY > 0) {
                  newy = y + mov;
              }
              if (y - mouseY < 0) {
                  newy = y - mov;
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
        //console.log(`Mouse X: ${event.clientX}, Mouse Y: ${event.clientY}`); // pour debug (fait lagger)
    });
});