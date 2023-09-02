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



def registrarPersonaje(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen, descripcion):
    sql = "INSERT INTO personaje (nombre, raza, subraza, clase, nivel, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, experiencia, estados, vida, mana, sexo, imagen, descripcion, vidaActual, manaActual) VALUES (%s, %s, %s, %s, 1, %s, %s, %s, %s, %s, %s, 0, 'Normal', 100, 100, %s, %s, %s, 100, 100)"
    val = (nombre, raza, subraza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo ,imagen, descripcion)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personajes()

def updatePersonaje(id, nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen, descripcion):
    sql = "UPDATE personaje SET nombre = %s, raza = %s, subraza = %s, clase = %s, constitucion = %s, fuerza = %s, destreza = %s, inteligencia = %s, sabiduria = %s, carisma = %s, sexo = %s, imagen = %s, descripcion = %s WHERE id = %s"
    val = (nombre, raza, subraza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo ,imagen, descripcion, id)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personaje(id)

@app.route('/update_personaje', methods=['POST'])
def update_personaje():
    if request.method == 'POST':
        id = request.form['id']
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
        else:
            imagen.filename = None
        return updatePersonaje(id, nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen.filename, descripcion)
    
@app.route('/restarVida', methods=['POST'])
def restarVida():
    if request.method == 'POST':
        id = request.form['id']
        vida = request.form['vida']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE personaje SET vidaActual = vidaActual - %s WHERE id = %s',[vida, id])
        mysql.connection.commit()
        return personaje(id) 

@app.route('/curar', methods=['POST'])
def curar():
    if request.method == 'POST':
        id = request.form['id']
        vida = request.form['vida']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE personaje SET vidaActual = vidaActual + %s WHERE id = %s',[vida, id])
        mysql.connection.commit()
        return personaje(id)
    
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
        else:
            imagen.filename = None
        return registrarPersonaje(nombre, raza, subraza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen.filename, descripcion)


def pj(data):
    personaje = {
        "id": data[0][0],
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
        "imagen": data[0][17],
        "descripcion": data[0][18],
        "vidaActual": data[0][19],
        "manaActual": data[0][20]
    }
    return personaje

def personajesData(data):
    personajes = []
    for i in data:
        personaje = {
            "id": i[0],
            "nombre": i[1],
            "raza": i[2],
            "razaNombre": getRaza(i[2]),
            "subraza": i[3],
            "clase": i[4],
            "claseNombre": clases.get(i[4]).get("nombre"),
            "nivel": i[5],
            "constitucion": i[6],
            "fuerza": i[7],
            "destreza": i[8],
            "inteligencia": i[9],
            "sabiduria": i[10],
            "carisma": i[11],
            "experiencia": i[12],
            "estados": i[13],
            "vida": i[14],
            "mana": i[15],
            "sexo": i[16],
            "imagen": i[17],
            "descripcion": i[18],
            "vidaActual": i[19],
            "manaActual": i[20]
        }
        personajes.append(personaje)
    return personajes


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

def bonificadoresAtributos(pj):
    bonificaciones = {
        "constitucion": (pj.get("constitucion")-10)//2,
        "fuerza": (pj.get("fuerza")-10)//2,
        "destreza": (pj.get("destreza")-10)//2,
        "inteligencia": (pj.get("inteligencia")-10)//2,
        "sabiduria": (pj.get("sabiduria")-10)//2,
        "carisma": (pj.get("carisma")-10)//2
    }

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

def getRaza(raza):
    return razas.get(raza).get("nombre")

@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/personajes')
def personajes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personaje')
    data = cur.fetchall()
    personajesSeleccionados = personajesData(data)
    return render_template('characters.html', personajes = personajesSeleccionados)

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
    razaPersonaje = getRaza(personajeSeleccionado.get("raza"))
    bonifRaza = bonifTotalesRaza(personajeSeleccionado)
    bonifClase = bonificacionesClaseTotal(clases.get(personajeSeleccionado.get("clase")).get("competenciaSalvacion"))
    competencias = clases.get(personajeSeleccionado.get("clase")).get("competencias")
    dado = clases.get(personajeSeleccionado.get("clase")).get("dadoVida")
    habilidadesEspeciales = clases.get(personajeSeleccionado.get("clase")).get("habilidadesEspeciales")
    porcentajeVida = 100-((personajeSeleccionado.get("vidaActual")/personajeSeleccionado.get("vida"))*100) 
    bonifAtributos = bonificadoresAtributos(personajeSeleccionado)
    return render_template('character.html', personaje = personajeSeleccionado, bonificacionAtributos = bonifAtributos,razaPersonaje = razaPersonaje, vidaAct = porcentajeVida, atributosPersonaje = atributosPersonaje,bonificacionesRaza = bonifRaza, bonificacionesClase = bonifClase, competencias = competencias, dado = dado, habilidadesEspeciales = habilidadesEspeciales)


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000
