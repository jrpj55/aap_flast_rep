
from flask import Flask, render_template
app= Flask(__name__)


@app.route('/')
def principal():
    return(render_template('index.html'))

@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes=("PHP", "Python", "Html", "C++", "Pascal", "Cobol", "Java", "JavaScript")
    return(render_template('lenguajes.html', Lenguaje_enviar = misLenguajes))

@app.route('/contacto')
def contacto():
    return(render_template('contacto.html'))

if __name__=='__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)

