var light = true

function init() {
  var elementsor = document.getElementsByClassName('btn-7');
  for (var element in elementsor) { // on initialise la couleur des boutons
    if (Number.isInteger(parseInt(element))) {
      elementsor[element].style.setProperty('--background-color-gradient', 'linear-gradient(0deg, #ff9700 0%, #fb4b02 100%)');
      elementsor[element].style.setProperty('--background-color-fix', '#fb4b02');
    }
  }
}


function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time)); // crée une promise pour l'async au bout d'un temps time
}

function backgroundcanvas(mouseX, mouseY) {
    const canvas = document.getElementById("canvas");
    canvas.width = window.innerWidth; // mettre à la taille de la fenêtre
    canvas.height = document.documentElement.scrollHeight-100; // Pour qu'il compte aussi les zones auquels on peut acceder en scrollant (-100 pour qu'il ne dépasse pas)
    var bounds = canvas.getBoundingClientRect();
    mouseX = mouseX - bounds.left; // corriger la position de la souris par rapport aux bords
    mouseY = mouseY - bounds.top;
    let space = 45; // espacement entre les points default=45
    const ctx = canvas.getContext("2d");
    for (let x = 0; x<canvas.width; x+=space) {
        for (let y = 0; y<canvas.height; y+=space) {
            let distance = Math.sqrt((mouseX-x)**2 + (mouseY-y)**2); //calcul de la distance
            /*if (distance > 125) {
                ctx.beginPath();
                ctx.arc(x, y, 1, 0, 2 * Math.PI, true); // on trace les points (cercle) normalement
                ctx.stroke();
            }*/
            if (distance < 20) { // les points partent trop loin après calcul (on les tracent pas)
                continue
            }
            else {
              let mov = (1000/distance)
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
              ctx.arc(newx, newy, 1, 0, 2 * Math.PI, true); // on trace les points (cercle)
              ctx.stroke();
            }
        }
    }
}

var running = false; // Pour empĉher le programme de se lancer plusieurs fois
      
async function spinFast() {
  if (running == false) { // Si la onction est déjà entrain de tourner ne pas la lancer
    running = true;
    console.log("spinning"); //pour print dans la console
    const object = document.querySelectorAll('.ele');
    for (let i = 2; i > 1.5; i=i-0.01) {
      t= 4-(i**2) // pour que l'animation deccélère plus i s'approche de sa vitesse max (i = 1)
      object.forEach(ele => { // Même chose qu'un "for ele in object:" en python
      animdel = ele.style['animation-delay']; // j'en ai besoin puisque la ligne suivante supprime cette valeur
      ele.style.animation='run ' + i + 's linear infinite'; // On change la vitesse d'animation
      ele.style['animation-delay'] = animdel;
      });
      await sleep(t);
    }
    object.forEach(ele => { // on remet à la normale
      animdel = ele.style['animation-delay'];
      ele.style.animation='run 2s linear infinite';
      ele.style['animation-delay'] = animdel;
      });
    await sleep(1000) // laisser un temps d'attente pour qu'il ne se déclenche pas imédiatemment
    running = false
  }
}
//background: linear-gradient(0deg, #ff9700 0%, #fb4b02 100%);
function changetheme() {
  var elementsbw = document.getElementsByClassName('themed-bw'); // tous les éléments possédant la classe themed-bw
  var elementsor = document.getElementsByClassName('btn-7');
  if (light == true) {
    light = false;
    var bw = '#666666';
    var orgrad = 'linear-gradient(0deg, rgba(142,36,3,1) 0%, rgba(99,17,15,1) 100%)';
    var orfix = "rgba(99,17,15,1)";
  }
  else {
    light = true;
    var bw = 'white';
    var orgrad = 'linear-gradient(0deg, #ff9700 0%, #fb4b02 100%)';
    var orfix = "#fb4b02";
  }
  ///////////// Le blanc /////////////
  document.body.style.backgroundColor = bw; // La couleur de fond de la page entière
  for (var element in elementsbw) {
    if (Number.isInteger(parseInt(element))) { // vérifie si la string correspond à un nombre en la transformant tous d'abord (element contient aussi length etc)
      elementsbw[element].style.backgroundColor = bw;
      //elements[element].style.borderColor = bw; // pour les bordures
    }
  }
  
  ///////////// L'orange /////////////
    for (var element in elementsor) {
    if (Number.isInteger(parseInt(element))) { // vérifie si la string correspond à un nombre en la transformant tous d'abord (element contient aussi length etc)
      elementsor[element].style.setProperty('--background-color-gradient', orgrad);
      elementsor[element].style.setProperty('--background-color-fix', orfix);
    }
  }
}


window.addEventListener("DOMContentLoaded", function(){ // on attend que le DOM se charge
  init();
  document.addEventListener('mousemove', (event) => {
    backgroundcanvas(event.clientX, event.clientY);
    //console.log(`Mouse X: ${event.clientX}, Mouse Y: ${event.clientY}`); // pour debug (fait lagger la console)
  });
  var dna = document.querySelector('.dna');
  dna.addEventListener("mouseover", () => {spinFast()});
  var themebtn = document.getElementById("flexSwitchCheckDefault");
  themebtn.addEventListener('click', event => {changetheme()});
});


function copy_gendata(objclass){ // prend en argument la class du texte de tag <p> et d'id = "gendata"
  var val = document.getElementsByClassName(objclass).gendata.innerText; // on accede au text dans l'élément
   // On copie
  navigator.clipboard.writeText(val);
  alert("C'est copié ! \n")
}