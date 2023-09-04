"use strict";

import { razas } from "./razas.js";
import { subrazas } from "./subrazas.js";
import {clases} from "./clases.js";
import {habilidades} from "./habilidades.js";

let bonifFuerzaRaza = 0;
let bonifFuerzaSubraza = 0;
let bonifFuerzaClase = 0;
let bonifFuerzaPuntos = 0;

let bonifDestrezaRaza = 0;
let bonifDestrezaSubraza = 0;
let bonifDestrezaClase = 0;
let bonifDestrezaPuntos = 0;

let bonifConstitucionRaza = 0;
let bonifConstitucionSubraza = 0;
let bonifConstitucionClase = 0;
let bonifConstitucionPuntos = 0;

let bonifInteligenciaRaza = 0;
let bonifInteligenciaSubraza = 0;
let bonifInteligenciaClase = 0;
let bonifInteligenciaPuntos = 0;

let bonifSabiduriaRaza = 0;
let bonifSabiduriaSubraza = 0;
let bonifSabiduriaClase = 0;
let bonifSabiduriaPuntos = 0;

let bonifCarismaRaza = 0;
let bonifCarismaSubraza = 0;
let bonifCarismaClase = 0;
let bonifCarismaPuntos = 0;


function getBonifTotalCarisma(){
    return bonifCarismaRaza + bonifCarismaSubraza + bonifCarismaClase + bonifCarismaPuntos;
}

function getBonifTotalSabiduria(){
    return bonifSabiduriaRaza + bonifSabiduriaSubraza + bonifSabiduriaClase + bonifSabiduriaPuntos;
}

function getBonifTotalInteligencia(){
    return bonifInteligenciaRaza + bonifInteligenciaSubraza + bonifInteligenciaClase + bonifInteligenciaPuntos;
}

function getBonifTotalConstitucion(){
    return bonifConstitucionRaza + bonifConstitucionSubraza + bonifConstitucionClase + bonifConstitucionPuntos;
}

function getBonifTotalDestreza(){
    return bonifDestrezaRaza + bonifDestrezaSubraza + bonifDestrezaClase + bonifDestrezaPuntos;
}

function getBonifTotalFuerza(){
    return bonifFuerzaRaza + bonifFuerzaSubraza + bonifFuerzaClase + bonifFuerzaPuntos;
}


const idPuntos = {
    fuerza: "bonifFuerza",
    destreza: "bonifDestreza",
    constitucion: "bonifConstitucion",
    inteligencia: "bonifInteligencia",
    sabiduria: "bonifSabiduria",
    carisma: "bonifCarisma"
}

function bonifInnerText(id, valor){
    let bonif = document.getElementById(id);
    if(valor >= 0){
        bonif.innerText = "+ " + valor;
    }else{
        bonif.innerText = valor;
    }
}

function diccComp(habilidad){
    let dicc = {
        "Acrobacias": "bonifAcrobacia",
        "Juego de manos": "bonifJuegoDeManos",
        "Sigilo": "bonifSigilo",
        "Atletismo": "bonifAtletismo",
        "Arcanos": "bonifArcanos",
        "Historia": "bonifHistoria",
        "Investigación": "bonifInvestigacion",
        "Naturaleza": "bonifNaturaleza",
        "Religión": "bonifReligion",
        "Percepción": "bonifPercepcion",
        "Medicina": "bonifMedicina",
        "Trato con animales": "bonifManejoDeAnimales",
        "Supervivencia": "bonifSupervivencia",
        "Perspicacia": "bonifAveriguarIntenciones",
        "Engaño": "bonifEngaño",
        "Intimidación": "bonifIntimidacion",
        "Persuasión": "bonifPersuasion",
    }
    return dicc[habilidad];
}


function actualizarCompetencias(){
    let claseSeleccionada = clases[$("#clase").val()];

    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        let comp = document.getElementById(diccComp(checkbox.value));
        for (const categoria in habilidades) {
            if (habilidades.hasOwnProperty(categoria)) {
              const habilidadesDeCategoria = habilidades[categoria];
              
              for (const habilidad of habilidadesDeCategoria) {
                if(checkbox.value === habilidad){
                    let b = getBonif(categoria);
                    if(checkbox.checked){
                        if(b+2<0){
                            comp.innerText = b+2;
                        }
                        else{
                            comp.innerText = "+ " + (b+2);
                        }
                    }else{
                        if(b<0){
                            comp.innerText = b;
                        }
                        else{
                            comp.innerText = "+ " + b;
                        }
                    }
                }
              }
            }
          }
    });
}

function getBonif(categoria){
    switch(categoria){
        case "destreza":
            return getBonifTotalDestreza();
        case "fuerza":
            return getBonifTotalFuerza();
        case "inteligencia":
            return getBonifTotalInteligencia();
        case "sabiduria":
            return getBonifTotalSabiduria();
        case "carisma":
            return getBonifTotalCarisma();
        case "constitucion":
            return getBonifTotalConstitucion();
    }
}


function actualizarBonificador(){
    let bonif = document.getElementById("bonifConstitucion");
    let vA = getBonifTotalConstitucion();
    bonifInnerText("bonifConstitucion", vA)

    bonif = document.getElementById("bonifFuerza");
    vA = getBonifTotalFuerza();
    bonifInnerText("bonifFuerza", vA);

    bonif = document.getElementById("bonifDestreza");
    vA = getBonifTotalDestreza();
    bonifInnerText("bonifDestreza", vA);

    bonif = document.getElementById("bonifInteligencia");
    vA = getBonifTotalInteligencia();
    bonifInnerText("bonifInteligencia", vA);

    bonif = document.getElementById("bonifSabiduria");
    vA = getBonifTotalSabiduria();
    bonifInnerText("bonifSabiduria", vA);

    bonif = document.getElementById("bonifCarisma");
    vA = getBonifTotalCarisma();
    bonifInnerText("bonifCarisma", vA);

    actualizarCompetencias();

}

const bonusBonificadores = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3]

var puntosTotal = 27;
const puntos = document.getElementById("puntosTotal");
puntos.textContent = puntosTotal;

var botonEnviar = document.querySelector("botonEnviar");


var razaActual;
const razaContainer = document.getElementById("raza");
const claseContainer = document.getElementById("clase");
let selectRaza = document.getElementById("raza");

$(document).ready(function() {
    const limit = 8;
// ACOMODAR ESTO PARA QUE SEA MAS LIMPIO (Y NO ANDA)
    function decrement(inputId) {
        const input = document.getElementById(inputId);
        if (input.value > limit && puntosTotal < 27) {
            input.value--;
            puntosTotal++;
            instanciarBonificadorPuntos(bonusBonificadores[input.value - 1], idPuntos[inputId]);
            actualizarBonificador();
            $("#puntosTotal").text(puntosTotal);
        }
    }
    $(".menosBoton").on("click", function() {
        const caracteristica = $(this).data("caracteristica");
        decrement(caracteristica);
    });
});

function instanciarBonificadorPuntos(bonificador, id){
    switch(id){
        case "bonifFuerza":
            bonifFuerzaPuntos = bonificador;
            break;
        case "bonifDestreza":
            bonifDestrezaPuntos = bonificador;
            break;
        case "bonifConstitucion":
            bonifConstitucionPuntos = bonificador;
            break;
        case "bonifInteligencia":
            bonifInteligenciaPuntos = bonificador;
            break;
        case "bonifSabiduria":
            bonifSabiduriaPuntos = bonificador;
            break;
        case "bonifCarisma":
            bonifCarismaPuntos = bonificador;
            break;
    }
}


$(document).ready(function() {
    const limit = 15;

    function increment(inputId) {
        const input = document.getElementById(inputId);
        if (input.value < limit && puntosTotal > 0) {
            puntosTotal--;
            input.value++;
            instanciarBonificadorPuntos(bonusBonificadores[input.value - 1], idPuntos[inputId]);
            actualizarBonificador();
            $("#puntosTotal").text(puntosTotal);
        }
    }

    $(".masBoton").on("click", function() {
        const caracteristica = $(this).data("caracteristica");
        increment(caracteristica);
    });
});

$("#creacionpj").on("submit", function(event) {
    if (puntosTotal != 0) {
        event.preventDefault(); // Evita el envío del formulario
        // Muestra el mensaje de advertencia
        $("#mensajeAdvertencia").text("Falta asignar puntos antes de enviar el formulario.");
    }
    
});


$(document).ready(function(){
    $("#clase").on("change", function(){
        let claseSeleccionada = clases[$("#clase").val()];

        // Esto esta de mas::::::::::::::::::::::::::::::::::::::
        let bonificadores = bonificadoresClase(claseSeleccionada);

        
        // Obtener todos los checkboxes
        var checkboxes = document.querySelectorAll('input[type="checkbox"]');

        // Establecer el máximo de checkboxes habilitados y el máximo seleccionable
        var maxHabilitados = claseSeleccionada.habilidades.length;

        checkboxes.forEach(checkbox => {
            checkbox.disabled = true;
            checkbox.checked = false;
        });

        checkboxes.forEach(checkbox => {
            if (claseSeleccionada.habilidades.includes(checkbox.value) || maxHabilitados === 0) {
                checkbox.disabled = false;
            }

            // Verificar el máximo seleccionable
            checkbox.addEventListener('change', () => {
                let claseSelec = clases[$("#clase").val()];
              

                    var maxSeleccionables = claseSelec.aElegir;
                    var seleccionadosActualmente = document.querySelectorAll('input[type="checkbox"]:checked').length;
                    if (checkbox.checked) {
                        if (seleccionadosActualmente <= maxSeleccionables) {
                            checkbox.checked = true;
                        } else {
                            checkbox.checked = false;
                        }
                    } 
                actualizarCompetencias()
                
            });

            bonifConstitucionClase = bonificadores.constitucion
            actualizarBonificador("bonifConstitucion");
            bonifFuerzaClase = bonificadores.fuerza
            actualizarBonificador("bonifFuerza");
            bonifDestrezaClase = bonificadores.destreza
            actualizarBonificador("bonifDestreza");
            bonifInteligenciaClase = bonificadores.inteligencia
            actualizarBonificador("bonifInteligencia");
            bonifSabiduriaClase = bonificadores.sabiduria
            actualizarBonificador("bonifSabiduria");
            bonifCarismaClase = bonificadores.carisma
            actualizarBonificador("bonifCarisma");

        });
    });
});

selectRaza.addEventListener("change", function(){
    let razaSeleccionada = razas[selectRaza.value];
    razaActual = razas[selectRaza.value];

    bonifConstitucionRaza = razaSeleccionada.constitucion;
    actualizarBonificador("bonifConstitucion");
    bonifFuerzaRaza = razaSeleccionada.fuerza;
    actualizarBonificador("bonifFuerza");
    bonifDestrezaRaza = razaSeleccionada.destreza;
    actualizarBonificador("bonifDestreza");
    bonifInteligenciaRaza = razaSeleccionada.inteligencia;
    actualizarBonificador("bonifInteligencia");
    bonifSabiduriaRaza = razaSeleccionada.sabiduria;
    actualizarBonificador("bonifSabiduria");
    bonifCarismaRaza = razaSeleccionada.carisma;
    actualizarBonificador("bonifCarisma");
})

function actualizarDOM(){
    $(document).ready(function(){
        function actualizarDatos(){

            let subrazaSeleccionada = $(".subraza-select").val(); 
            let subrazaSeleccionadaObj = subrazas[objKey(razaActual)].find(subraza => subraza.nombre === subrazaSeleccionada);
            let predeterminado = 0;
            let constitucion = subrazaSeleccionadaObj.puntosExtras.constitucion || predeterminado;
            let fuerza = subrazaSeleccionadaObj.puntosExtras.fuerza || predeterminado;
            let destreza = subrazaSeleccionadaObj.puntosExtras.destreza || predeterminado;
            let inteligencia = subrazaSeleccionadaObj.puntosExtras.inteligencia || predeterminado;
            let sabiduria = subrazaSeleccionadaObj.puntosExtras.sabiduria || predeterminado;
            let carisma = subrazaSeleccionadaObj.puntosExtras.carisma || predeterminado;

            bonifConstitucionSubraza = constitucion;
            actualizarBonificador("bonifConstitucion");
            bonifFuerzaSubraza = fuerza;
            actualizarBonificador("bonifFuerza");
            bonifDestrezaSubraza= destreza;
            actualizarBonificador("bonifDestreza");
            bonifInteligenciaSubraza = inteligencia; 
            actualizarBonificador("bonifInteligencia");
            bonifSabiduriaSubraza = sabiduria;    
            actualizarBonificador("bonifSabiduria");
            bonifCarismaSubraza = carisma;
            actualizarBonificador("bonifCarisma");


        }
        $(".subraza-select").on("change", actualizarDatos);
    });
}

function bonificadoresClase(claseSeleccionada){
    let bonificadoresClase = {
        constitucion: 0,
        fuerza: 0,
        destreza: 0,
        inteligencia: 0,
        sabiduria: 0,
        carisma: 0
    }


    return bonificadoresClase;
}



function valorActual(elemento){
    let valor = elemento.split(" ");
    return parseInt(valor[1]);
}



for (const raza in razas) {
    const option = document.createElement("option");
    option.value = raza;
    option.text = razas[raza].nombre;
    razaContainer.appendChild(option);
}
    




for(const clase in clases){
    const option = document.createElement("option");
    option.value = clase;
    option.text = clases[clase].nombre;
    claseContainer.appendChild(option);
}




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
            defaultOption.disabled = true; // Agregar el atributo disabled
            defaultOption.selected = true; // Agregar el atributo selected
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

function objKey(obj){
    const keys = Object.keys(razas);
    for(const k of keys){
        if(razas[k] === obj){
            return k;
        }
    }
}
