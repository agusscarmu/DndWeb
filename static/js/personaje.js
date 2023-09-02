"use strict";

function openDiv(divId) {
    var divToShow = document.getElementById(divId);
    if (divToShow.style.display === "none" || divToShow.style.display === "") {
        divToShow.style.display = "block";
    } else {
        divToShow.style.display = "none";
    }
}

function closeDiv(id){
    document.getElementById(id).style.display = "none";
}

const liquidoElement = document.querySelector('.liquido');
const vidaAct = liquidoElement.getAttribute('data-vida');
const vidaActNum = parseInt(vidaAct);
liquidoElement.style.setProperty('--liquido', `${vidaAct}%`);