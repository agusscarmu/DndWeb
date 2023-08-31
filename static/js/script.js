"use strict";

let tarjetaPersonaje = document.querySelectorAll(".tarjetapj");
let imagenPersonaje = document.querySelectorAll(".imagen");

for(let i = 0; i < tarjetaPersonaje.length; i++){
tarjetaPersonaje[i].addEventListener("mouseover", function(){
    if(tarjetaPersonaje[i] && imagenPersonaje){
        tarjetaPersonaje[i].classList.add("tarjetapj-hover");
        imagenPersonaje[i].classList.add("tarjetapj-img-hover");
    }
})

tarjetaPersonaje[i].addEventListener("mouseout", function(){
    if(tarjetaPersonaje[i] && imagenPersonaje){
        tarjetaPersonaje[i].classList.remove("tarjetapj-hover");
        imagenPersonaje[i].classList.remove("tarjetapj-img-hover");
    }
})
}

let logo = document.getElementById("logoDado");


logo.addEventListener("mouseover", function(){
    logo.classList.add("logo-hover");
});

logo.addEventListener("mouseout", function(){
    logo.classList.remove("logo-hover");
});

