from flask import Flask, render_template, request, send_from_directory,url_for, redirect
from flask_mysqldb import MySQL
from razas_data import razas
from subrazas_data import subrazas
from clases_data import clases
import os


app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dnd'

mysql = MySQL(app)


def registrarPersonaje(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma):
    sql = "INSERT INTO personaje (nombre, raza, subraza, clase, nivel, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, experiencia, estados, vida, mana, sexo) VALUES (%s, %s, %s, %s, 1, %s, %s, %s, %s, %s, %s, 0, 'Normal', 100, 100, %s)"
    val = (nombre, raza, subraza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personajes()

def registrarPersonajeF(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen):
    sql = "INSERT INTO personaje (nombre, raza, subraza, clase, nivel, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, experiencia, estados, vida, mana, sexo, imagen) VALUES (%s, %s, %s, %s, 1, %s, %s, %s, %s, %s, %s, 0, 'Normal', 100, 100, %s, %s)"
    val = (nombre, raza, subraza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo ,imagen)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personajes()

@app.route('/add_personaje', methods=['POST'])
def add_personaje():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        try:
            subraza = request.form['subraza']
        except:
            subraza = None
        sexo = request.form['sexo']
        clase = request.form['clase']
        constitucion = request.form['constitucion'] 
        fuerza = request.form['fuerza']
        destreza = request.form['destreza']
        inteligencia = request.form['inteligencia']
        sabiduria = request.form['sabiduria']
        carisma = request.form['carisma']
        descripcion = request.form['descripcion']
        imagen = request.files['imagen']
        if imagen.filename!='':
            imagen.save(os.path.join(app.root_path, 'static\imagenesPersonajes', imagen.filename))
            return registrarPersonajeF(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen.filename)
        else:
            return registrarPersonaje(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma)

def pj(data):
    personaje = {
        "nombre": data[0][1],
        "raza": data[0][2],
        "subraza": data[0][3],
        "clase": data[0][4],
        "nivel": data[0][5],
        "constitucion": data[0][6],
        "fuerza": data[0][7],
        "destreza": data[0][8],
        "inteligencia": data[0][9],
        "sabiduria": data[0][10],
        "carisma": data[0][11],
        "experiencia": data[0][12],
        "estados": data[0][13],
        "vida": data[0][14],
        "mana": data[0][15],
        "sexo": data[0][16],
        "imagen": data[0][17]
    }
    return personaje

def bonificacionRaza(raza, atributo):
    if raza == None:
        return 0
    else:
        return razas.get(raza).get(atributo)
    
def bonificacionSubRaza(raza, subraza, atributo):
    if subraza == None:
        return 0
    else:
        for i in subrazas.get(raza):
            if i.get("nombre") == subraza:
                if atributo in i.get("puntosExtras"):
                    return i.get("puntosExtras").get(atributo)
        return 0

def bonifTotalesRaza(pj):
    bonificaciones = {
        "constitucion": bonificacionRaza(pj.get("raza"), "constitucion") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "constitucion"),
        "fuerza": bonificacionRaza(pj.get("raza"), "fuerza") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "fuerza"),
        "destreza": bonificacionRaza(pj.get("raza"), "destreza") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "destreza"),
        "inteligencia": bonificacionRaza(pj.get("raza"), "inteligencia") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "inteligencia"),
        "sabiduria": bonificacionRaza(pj.get("raza"), "sabiduria") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "sabiduria"),
        "carisma": bonificacionRaza(pj.get("raza"), "carisma") + bonificacionSubRaza(pj.get("raza"), pj.get("subraza"), "carisma")
    }
    return bonificaciones

def bonificacionesClaseTotal(clase):
    bonificaciones = {
        "constitucion": 0,
        "fuerza": 0,
        "destreza": 0,
        "inteligencia": 0,
        "sabiduria": 0,
        "carisma": 0
    }

    for bonificacion in clase:
        bonificaciones[bonificacion] = 2

    return bonificaciones

def atributosPj(personaje):
    atributos = {
        "constitucion": personaje.get("constitucion"),
        "fuerza": personaje.get("fuerza"),
        "destreza": personaje.get("destreza"),
        "inteligencia": personaje.get("inteligencia"),
        "sabiduria": personaje.get("sabiduria"),
        "carisma": personaje.get("carisma")
    }

    return atributos

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/personajes')
def personajes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personaje')
    data = cur.fetchall()
    return render_template('characters.html', personajes = data)

@app.route('/creacion')
def creacion():
    return render_template('createCharacter.html')

@app.route('/eliminar')
def eliminar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personaje')
    data = cur.fetchall()
    return render_template('eliminar.html', personajes = data)

@app.route('/eliminar/<id>')
def eliminarPersonaje(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM personaje WHERE id = %s',[id])
    mysql.connection.commit()
    return redirect(url_for('eliminar'))

@app.route('/reglamento')
def reglamento():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'elems/D&D5Manual.pdf')

@app.route('/personaje/<id>')
def personaje(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personaje WHERE id = %s',[id])
    data = cur.fetchall()
    print(data)
    personajeSeleccionado = pj(data)
    atributosPersonaje = atributosPj(personajeSeleccionado)
    bonifRaza = bonifTotalesRaza(personajeSeleccionado)
    bonifClase = bonificacionesClaseTotal(clases.get(personajeSeleccionado.get("clase")).get("competenciaSalvacion"))
    competencias = clases.get(personajeSeleccionado.get("clase")).get("competencias")
    dado = clases.get(personajeSeleccionado.get("clase")).get("dadoVida")
    habilidadesEspeciales = clases.get(personajeSeleccionado.get("clase")).get("habilidadesEspeciales")
    return render_template('character.html', personaje = personajeSeleccionado, atributosPersonaje = atributosPersonaje,bonificacionesRaza = bonifRaza, bonificacionesClase = bonifClase, competencias = competencias, dado = dado, habilidadesEspeciales = habilidadesEspeciales)


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000
