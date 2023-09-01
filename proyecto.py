from flask import Flask, render_template, send_from_directory
import os

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/personajes')
def personajes():
    return render_template('characters.html')

@app.route('/creacion')
def creacion():
    return render_template('createCharacter.html')

@app.route('/reglamento')
def reglamento():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'elems/D&D5Manual.pdf')


if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000
