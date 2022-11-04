var light = true;
var start = false;
var running = false; // Pour empĉher SpinFast() de se lancer plusieurs fois

function initTheme() {
  if (document.cookie == 'darkmode=true') {
    document.getElementById('mainstyle').setAttribute('href', "static/css/maindark.css"); // l'utilisateur est en darkmode
  }
  else {
    document.cookie = 'darkmode=false'; // Au cas où le cookie n'existe pas encore
  }
}

function nooverflow () {
  if (document.body.scrollHeight < 1100) { // Si la fenêtre est trop petite
    document.getElementsByClassName('nowindowoverflow')['0'].style.display = "none"; // l'alpiniste ne sera pas généré
  }
}

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time)); // crée une promise pour l'async au bout d'un temps time, permet donc de mettre en pause la fonction
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
            if (distance < 20) { // les points partent trop loin après calcul (on ne les tracent pas)
                continue;
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

/*Désactivé puisque il était impossible de modifier la vitesse sans que cela paraisse étrange
function spin() {
  if (start==true) {
    spinFast();
  }
  const object = document.querySelectorAll('.ele');
  object.forEach(ele => { // on remet à la normale
      animdel = ele.style['animation-delay'];
      ele.style.animation='run 2s linear 1';
      ele.style['animation-delay'] = animdel;
      });
}


async function spinFast() {
  if (running == false) { // Si la fonction est déjà entrain de tourner ne pas la lancer
    running = true;
    console.log("spinning"); //pour print dans la console
    const object = document.querySelectorAll('.ele');
    object.forEach(ele => { // on remet à la normale
      animdel = ele.style['animation-delay'];
      ele.style.animation='run 2s ease-in-out infinite';
      ele.style['animation-delay'] = animdel;
      sleep(150);
      });
    await sleep(1000); // temps d'attente
    running = false;
    start = false;
  }
}
*/

function changetheme() {
  var stylesheet = document.getElementById('mainstyle'); // On cherche le tag du lien vers main.css
  if ("darkmode=false" == document.cookie) {
    light = false;
    document.cookie = "darkmode=true"; // On enregistre son theme pour le changement de page
    stylesheet.setAttribute('href', "static/css/maindark.css"); // On change le css pour la stylesheet dark mode
  }
  else {
    light = true;
    document.cookie = "darkmode=false";
    stylesheet.setAttribute('href', "static/css/main.css");
  }
}

function copy_gendata(objclass){ // prend en argument la class du texte de tag <p> et d'id = "gendata"
  var val = document.getElementsByClassName(objclass).gendata.innerText; // on accede au text dans l'élément
   // On copie
  navigator.clipboard.writeText(val);
  alert("C'est copié ! \n");
}

window.addEventListener("DOMContentLoaded", function(){ // on attend que le DOM se charge
  initTheme(); // pour changer le theme lors du chargement d'une nouvelle page
  document.addEventListener('mousemove', (event) => { // exécute à chaque event : mousemove
    backgroundcanvas(event.clientX, event.clientY); // prend en argument la position de la souris
    //console.log(`Mouse X: ${event.clientX}, Mouse Y: ${event.clientY}`); // pour debug (!!! fait lagger la console)
  });
  var themebtn = document.getElementById("flexSwitchCheckDefault");
  themebtn.addEventListener('click', event => {changetheme()});
  const dna = document.querySelector('.dna');
  dna.addEventListener("mousemove", () => {start=true}); // pour Spin qui ne fonctionne pas
  nooverflow(); // ne génère pas certain éléments pour ne pas rajouter de scrollbar
});

/*
async function main() { // DANGER fait crash pas seulement le navigateur mais aussi l'ordinateur NE PAS TOUCHER
  while (true) {
    await spin();
    console.log('hi')
  }
}
main();*/