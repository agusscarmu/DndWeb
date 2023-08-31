import { conexion } from './conexion.js';

const express = require('express');
const app = express();

// Configura el middleware para analizar el cuerpo de la solicitud
app.use(express.urlencoded({ extended: true }));

// Ruta para manejar el envío del formulario
app.post('/insertar', function(req, res) {
    const formulario = {
        nombre: req.body.nombre,
        raza: req.body.raza,
        subraza: req.body.subraza,
        sexo: req.body.sexo,
        clase: req.body.clase,
        constitucion: req.body.constitucion,
        fuerza: req.body.fuerza,
        destreza: req.body.destreza,
        inteligencia: req.body.inteligencia,
        sabiduria: req.body.sabiduria,
        carisma: req.body.carisma,
        descripcion: req.body.descripcion,
    };

    const query = 'INSERT INTO `personaje`(`nombre`, `raza`, `clase`, `nivel`, `constitucion`, `fuerza`, `destreza`, `inteligencia`, `sabiduria`, `carisma`, `experiencia`, `vida`, `mana`) VALUES(?,?,?,1,?,?,?,?,?,?,0,100,100)';

    if(formulario.subraza!=''){
        formulario.raza = formulario.subraza;
    }

    conexion.query(query, [formulario.nombre, formulario.raza, formulario.clase, formulario.constitucion, formulario.fuerza, formulario.destreza, formulario.inteligencia, formulario.sabiduria, formulario.carisma], function(error, resultados) {
        if (error) {
            throw error;
        }
        console.log('Datos insertados:', resultados);
        res.send('Datos insertados correctamente');
    });
});
