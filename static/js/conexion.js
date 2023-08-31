var mysql = require('mysql');

var conexion = mysql.createConnection({
    host: 'localhost',
    database: 'Dnd',
    user: 'root',
    password: ''
});

conexion.connect(function(error){
    if(error){
        throw error;
    }else{
        console.log('Conexion correcta.');
    }
});


export { conexion };