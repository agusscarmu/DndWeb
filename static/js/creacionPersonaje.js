"use strict";
import { razas } from "./razas.js";
import { subrazas } from "./subrazas.js";

var puntosTotal = 27;
const puntos = document.getElementById("puntosTotal");
puntos.textContent = puntosTotal;


var razaActual;
const razaContainer = document.getElementById("raza");
    
    
    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.text = "Seleccione una raza";
    razaContainer.appendChild(defaultOption);
    
    for (const raza in razas) {
        const option = document.createElement("option");
        option.value = raza;
        option.text = razas[raza].nombre;
        razaContainer.appendChild(option);
    }
    

let selectRaza = document.getElementById("raza");

selectRaza.addEventListener("change", function(){
    let razaSeleccionada = razas[selectRaza.value];
    razaActual = razas[selectRaza.value];

    let bonifConstitucion = document.getElementById("bonifConstitucion");
    bonifConstitucion.innerText = "+ "+razaSeleccionada.constitucion;
    let bonifFuerza = document.getElementById("bonifFuerza");
    bonifFuerza.innerText = "+ "+razaSeleccionada.fuerza;
    let bonifDestreza = document.getElementById("bonifDestreza");
    bonifDestreza.innerText = "+ "+razaSeleccionada.destreza;
    let bonifInteligencia = document.getElementById("bonifInteligencia");
    bonifInteligencia.innerText = "+ "+razaSeleccionada.inteligencia;
    let bonifSabiduria = document.getElementById("bonifSabiduria");
    bonifSabiduria.innerText = "+ "+razaSeleccionada.sabiduria;
    let bonifCarisma = document.getElementById("bonifCarisma");
    bonifCarisma.innerText = "+ "+razaSeleccionada.carisma;
})
$(document).ready(function(){
    function mostrarSubrazas() {
        const selectRaza = $("#raza").val();
        const subrazasContainer = document.getElementById("subrazas-container");
        // Eliminar el contenido actual del contenedor
        subrazasContainer.innerHTML = '';
    
        const razaSubrazas = subrazas[selectRaza];
    
        if (razaSubrazas) {
            const span = document.createElement("span");
            span.innerText = "Subraza: ";
            subrazasContainer.appendChild(span);
    
            const subrazasSelect = document.createElement("select");
            subrazasSelect.className = "subraza-select";  // Utilizar una clase en lugar de id
            subrazasSelect.name = "subraza";
            subrazasSelect.required = true;
    
            const defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.text = "Seleccione una Sub-Raza";
            subrazasSelect.appendChild(defaultOption);
    
            razaSubrazas.forEach(function (subraza) {
                const opcion = document.createElement("option");
                opcion.value = subraza.nombre;
                opcion.text = subraza.nombre;
                subrazasSelect.appendChild(opcion);
            });
    
            subrazasContainer.appendChild(subrazasSelect);
            actualizarDOM();
        }
    }    
    $("#raza").on("change", mostrarSubrazas);
});

function actualizarDOM(){
    $(document).ready(function(){
        function actualizarDatos(){
            const subrazaSeleccionada = $(".subraza-select").val(); 
            const subrazaSeleccionadaObj = subrazas[objKey(razaActual)].find(subraza => subraza.nombre === subrazaSeleccionada);

            const constitucion = subrazaSeleccionadaObj.puntosExtras.constitucion;
            const fuerza = subrazaSeleccionadaObj.puntosExtras.fuerza;
            const destreza = subrazaSeleccionadaObj.puntosExtras.destreza;
            const inteligencia = subrazaSeleccionadaObj.puntosExtras.inteligencia;
            const sabiduria = subrazaSeleccionadaObj.puntosExtras.sabiduria;
            const carisma = subrazaSeleccionadaObj.puntosExtras.carisma;

            let bonifConstitucion = document.getElementById("bonifConstitucion");
            bonifConstitucion.innerText = "+ "+(razaActual.constitucion + punto(constitucion));
            let bonifFuerza = document.getElementById("bonifFuerza");
            bonifFuerza.innerText = "+ "+(razaActual.fuerza + punto(fuerza));
            let bonifDestreza = document.getElementById("bonifDestreza");
            bonifDestreza.innerText = "+ "+(razaActual.destreza + punto(destreza));
            let bonifInteligencia = document.getElementById("bonifInteligencia");
            bonifInteligencia.innerText = "+ "+(razaActual.inteligencia + punto(inteligencia));
            let bonifSabiduria = document.getElementById("bonifSabiduria");
            bonifSabiduria.innerText = "+ "+(razaActual.sabiduria + punto(sabiduria));
            let bonifCarisma = document.getElementById("bonifCarisma");
            bonifCarisma.innerText = "+ "+(razaActual.carisma + punto(carisma));
        }
        $(".subraza-select").on("change", actualizarDatos);
    });
}

function objKey(obj){
    const keys = Object.keys(razas);
    for(const k of keys){
        if(razas[k] === obj){
            return k;
        }
    }
}

function punto(valor){
    if(valor === undefined){
        return 0;
    }else{
        return valor;
    }
}

$(document).ready(function() {
    const limit = 15;

    function increment(inputId) {
        const input = document.getElementById(inputId);
        if (input.value < limit && puntosTotal > 0) {
            puntosTotal--;
            input.value++;
            $("#puntosTotal").text(puntosTotal);
        }
    }

    $(".masBoton").on("click", function() {
        const caracteristica = $(this).data("caracteristica");
        increment(caracteristica);
    });
});

$(document).ready(function() {
    const limit = 8;

    function decrement(inputId) {
        const input = document.getElementById(inputId);
        if (input.value > limit && puntosTotal < 27) {
            input.value--;
            puntosTotal++;
            $("#puntosTotal").text(puntosTotal);
        }
    }
    $(".menosBoton").on("click", function() {
        const caracteristica = $(this).data("caracteristica");
        decrement(caracteristica);
    });
});
