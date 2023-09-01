from flask import Flask, render_template, request, send_from_directory
from flask_mysqldb import MySQL
from razas_data import razas
from subrazas_data import subrazas
import os


app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dnd'

mysql = MySQL(app)

def registrarPersonaje(nombre, raza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma):
    sql = "INSERT INTO personaje (nombre, raza, clase, nivel, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, experiencia, estados, vida, mana, sexo) VALUES (%s, %s, %s, 1, %s, %s, %s, %s, %s, %s, 0, 'Normal', 100, 100, %s)"
    val = (nombre, raza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personajes()

def registrarPersonajeF(nombre, raza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen):
    sql = "INSERT INTO personaje (nombre, raza, clase, nivel, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, experiencia, estados, vida, mana, sexo, imagen) VALUES (%s, %s, %s, 1, %s, %s, %s, %s, %s, %s, 0, 'Normal', 100, 100, %s, %s)"
    val = (nombre, raza, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, sexo ,imagen)
    cur = mysql.connection.cursor()
    cur.execute(sql, val)
    mysql.connection.commit()
    return personajes()

@app.route('/add_personaje', methods=['POST'])
def add_personaje():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
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
            return registrarPersonajeF(nombre, raza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma, imagen.filename)
        else:
            return registrarPersonaje(nombre, raza, sexo, clase, constitucion, fuerza, destreza, inteligencia, sabiduria, carisma)

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
    clases=['Bárbaro', 'Bardo', 'Clérigo', 'Druida', 'Guerrero', 'Mago', 'Monje', 'Paladín', 'Pícaro', 'Hechicero', 'Brujo']
    return render_template('createCharacter.html', clases = clases)

@app.route('/reglamento')
def reglamento():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'elems/D&D5Manual.pdf')


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000
