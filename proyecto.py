from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)

