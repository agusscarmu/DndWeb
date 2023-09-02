"use strict";
import { razas } from "./razas.js";
import { subrazas } from "./subrazas.js";
import {clases} from "./clases.js";

var puntosTotal = 0;
const puntos = document.getElementById("puntosTotal");
puntos.textContent = puntosTotal;


var razaActual;
const razaContainer = document.getElementById("raza");
    

    
for (const raza in razas) {
    const option = document.createElement("option");
    option.value = raza;
    option.text = razas[raza].nombre;
    razaContainer.appendChild(option);
}
    

const claseContainer = document.getElementById("clase");


for(const clase in clases){
    const option = document.createElement("option");
    option.value = clase;
    option.text = clases[clase].nombre;
    claseContainer.appendChild(option);
}

let selectRaza = document.getElementById("raza");

selectRaza.addEventListener("change", function(){
    let razaSeleccionada = razas[selectRaza.value];
    razaActual = razas[selectRaza.value];

    actualizarBonificador("bonifConstitucion", razaSeleccionada.constitucion);
    actualizarBonificador("bonifFuerza", razaSeleccionada.fuerza);
    actualizarBonificador("bonifDestreza", razaSeleccionada.destreza);
    actualizarBonificador("bonifInteligencia", razaSeleccionada.inteligencia);
    actualizarBonificador("bonifSabiduria", razaSeleccionada.sabiduria);
    actualizarBonificador("bonifCarisma", razaSeleccionada.carisma);

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
            const predeterminado = 0;
            const constitucion = subrazaSeleccionadaObj.puntosExtras.constitucion || predeterminado;
            const fuerza = subrazaSeleccionadaObj.puntosExtras.fuerza || predeterminado;
            const destreza = subrazaSeleccionadaObj.puntosExtras.destreza || predeterminado;
            const inteligencia = subrazaSeleccionadaObj.puntosExtras.inteligencia || predeterminado;
            const sabiduria = subrazaSeleccionadaObj.puntosExtras.sabiduria || predeterminado;
            const carisma = subrazaSeleccionadaObj.puntosExtras.carisma || predeterminado;

            desactualizarBonificadorSubraza("bonifConstitucion");
            desactualizarBonificadorSubraza("bonifFuerza");
            desactualizarBonificadorSubraza("bonifDestreza");
            desactualizarBonificadorSubraza("bonifInteligencia");
            desactualizarBonificadorSubraza("bonifSabiduria");
            desactualizarBonificadorSubraza("bonifCarisma");


            actualizarBonificadorSubraza("bonifConstitucion", constitucion);
            actualizarBonificadorSubraza("bonifFuerza", fuerza);
            actualizarBonificadorSubraza("bonifDestreza", destreza);
            actualizarBonificadorSubraza("bonifInteligencia", inteligencia);
            actualizarBonificadorSubraza("bonifSabiduria", sabiduria);
            actualizarBonificadorSubraza("bonifCarisma", carisma);

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

function puntosSobra(puntosTotal, puntosUsados){
    return puntosTotal - puntosUsados;
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

$("#actualizarpj").on("submit", function(event) {
    if (puntosTotal != 0) {
        event.preventDefault(); // Evita el envío del formulario
        // Muestra el mensaje de advertencia
        $("#mensajeAdvertencia").text("Falta asignar puntos antes de enviar el formulario.");
    }
    
});
$(document).ready(function(){
    $("#clase").on("change", function(){
        let claseSeleccionada = clases[$("#clase").val()];
        let bonificadores = bonificadoresClase(claseSeleccionada);
        
        desactualizarBonificadorClase("bonifConstitucion");
        desactualizarBonificadorClase("bonifFuerza");
        desactualizarBonificadorClase("bonifDestreza");
        desactualizarBonificadorClase("bonifInteligencia");
        desactualizarBonificadorClase("bonifSabiduria");
        desactualizarBonificadorClase("bonifCarisma");

        actualizarBonificadorClase("bonifConstitucion", bonificadores.constitucion);
        actualizarBonificadorClase("bonifFuerza", bonificadores.fuerza);
        actualizarBonificadorClase("bonifDestreza", bonificadores.destreza);
        actualizarBonificadorClase("bonifInteligencia", bonificadores.inteligencia);
        actualizarBonificadorClase("bonifSabiduria", bonificadores.sabiduria);
        actualizarBonificadorClase("bonifCarisma", bonificadores.carisma);

    });
});


function bonificadoresClase(claseSeleccionada){
    let bonificadoresClase = {
        constitucion: 0,
        fuerza: 0,
        destreza: 0,
        inteligencia: 0,
        sabiduria: 0,
        carisma: 0
    }

    for(const caracteristica in bonificadoresClase){
        if(claseSeleccionada.competenciaSalvacion.includes(caracteristica)){
            bonificadoresClase[caracteristica] = 2;
        }
    }

    return bonificadoresClase;
}


function valorActual(elemento){
    let valor = elemento.split(" ");
    return parseInt(valor[1]);
}

var ultimosBonificadoresSubraza = {
    constitucion: 0,
    fuerza: 0,
    destreza: 0,
    inteligencia: 0,
    sabiduria: 0,
    carisma: 0
}

function actualizarBonificadorSubraza(id, bonificador) {
    let elemento = document.getElementById(id);
    let vA = valorActual(elemento.innerText) || 0; // Parseamos a número y manejamos NaN
    ultimosBonificadoresSubraza[id] = bonificador;
    elemento.innerText = "+ " + (vA + bonificador);
}


function desactualizarBonificadorSubraza(id) {
    let elemento = document.getElementById(id);
    let vA = valorActual(elemento.innerText) || 0; // Parseamos a número y manejamos NaN
    elemento.innerText = "+ " + (vA - ultimosBonificadoresSubraza[id]);
    ultimosBonificadoresSubraza[id] = 0;
}

function actualizarBonificador(id, bonificador) {
    desactualizarBonificadorSubraza(id);
    desactualizarBonificadorClase(id);
    let elemento = document.getElementById(id);
    elemento.innerText = "+ " + (bonificador);
}

var ultimosBonificadoresClase = {
    constitucion: 0,
    fuerza: 0,
    destreza: 0,
    inteligencia: 0,
    sabiduria: 0,
    carisma: 0
}

function actualizarBonificadorClase(id, bonificador){
    let elemento = document.getElementById(id);
    let vA = valorActual(elemento.innerText) || 0;
    ultimosBonificadoresClase[id] = bonificador;
    elemento.innerText = "+ " + (vA + bonificador);
}

function desactualizarBonificadorClase(id){
    let elemento = document.getElementById(id);
    let vA = valorActual(elemento.innerText) || 0;
    elemento.innerText = "+ " + (vA - ultimosBonificadoresClase[id]);
    ultimosBonificadoresClase[id] = 0;
}


