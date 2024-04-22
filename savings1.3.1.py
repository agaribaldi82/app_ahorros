from flask import Flask, render_template, request
import random
import pymysql

app = Flask(__name__)

numero_ale = 0
cur = None
conexion = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numero_random', methods=['POST'])
def numero_random():
    global numero_ale, cur, conexion
    numero_ale = random.randint(1, 366)

    # Conexion a MySQL, guardando el numero aleatorio en la base de datos.
    conexion = pymysql.connect(host='localhost', user='root', db='practicas')
    cur = conexion.cursor()
    cur.execute('INSERT INTO app_ahorro (numero, fecha) VALUES (%s, curdate())', (numero_ale,))
    conexion.commit()

    return render_template('index.html', numero_ale=numero_ale)

@app.route('/suma_ahorros', methods=['POST'])
def suma_ahorros():
    global cur, conexion
    cur.execute('SELECT SUM(numero) FROM app_ahorro')
    suma = cur.fetchone()[0]  # Extract the sum from the tuple
    conexion.commit()

    return render_template('index.html', suma=suma)

@app.route('/lista_numeros', methods=['POST'])
def lista_numeros():
    global cur, conexion
    lista= cur.execute('SELECT numero, fecha FROM app_ahorro')
    lista1 = cur.fetchall()

    results = []

    for numero, fecha in lista1:
        # Append each result to the list
        results.append((numero, fecha))


    return render_template('index.html', lista=lista)

if __name__ == '__main__':
    app.run(debug=True)