import tkinter as tk
import random

ventana = tk.Tk()
ventana.config(width=800, height=500, background='black')
ventana.title('Mis ahorros')

#Funcion para motrar en etiqueta "numero" el numero random y agregarlo a la lista para sumarlo, lo guardamos en DB:

def numero_random():
    global numero_ale
    global cur
    global conexion
    numero_ale = random.randint(1,366)
    numero.config(text=int(numero_ale))

    # Conexion a MySql, guardando el numero aleatorio en la base de datos.
    conexion = pymysql.connect(host='localhost', user='root', db='practicas')
    cur = conexion.cursor()
    cur.execute('insert into app_ahorro (numero, fecha) values (%s, curdate())', (numero_ale,))
    conexion.commit()
'''
    #Descartar numero repetido - NO FUNCIONA

    numeros_registrados = cur.execute('select numero from app_ahorro')
    numeros_endb = numeros_registrados.fetchall()
    if numero_ale in numeros_registrados:
        numero_ale = int(numero_ale)
        cur.execute('delete from app_ahorro order by numero desc limit 1')
        conexion.commit()

        return numero_random()

'''
#Funcion para mostrar en pantalla la suma de los numeros en la base de datos
#Curioso...si le ejecuto select * me devuelve la cantidad de registros
#Si le ejecuto select sum(numero) me devuelve siempre 1

def suma_ahorros():
    cur.execute('select sum(numero) from app_ahorro')
    sumas = cur.fetchone()[0]
    ahorro_etiqueta.config(text=(sumas))
    conexion.commit()

def historial():
    global cur, conexion
    cur.execute('SELECT numero, fecha FROM app_ahorro')
    lista = cur.fetchall()

    historial_text = ""

    for registro in lista:
        numero, fecha = registro
        historial_text += f"Numero: {numero}, Fecha: {fecha}\n"

    lista_ahorros.config(text=historial_text)

#Etiquetas y botones:

titulo = tk.Label(text='Ahorro del día:')
titulo.place(x=100, y=20, width=300, height=40)
titulo.config(background='light green', font=('Arial', 18), fg='black')

texto = tk.Label(text='Hoy te toca ahorrar:')
texto.place(x=100, y=100, width=300, height=40)
texto.config(background='black', font=('Arial', 16), fg='white')

numero = tk.Label(text='')
numero.place(x=100, y=150, width=300, height=40)
numero.config(background='white', font=('Arial', 16), fg='black')

numero_ahorro = tk.Label(text='Ahorrado a la fecha:')
numero_ahorro.place(x=100, y=220, width=300, height=40)
numero_ahorro.config(background='black', font=('Arial', 16), fg='white')

boton = tk.Button(text='$$$', command=numero_random)
boton.place(x=100, y=350, width=100, height=40)
boton.config(background='green', font=('Arial', 16), fg='white')

ahorro_etiqueta = tk.Label(text='')
ahorro_etiqueta.config(background='white', font=('Arial', 16))
ahorro_etiqueta.place(x=100, y=270, width=300, height=40)

boton2 = tk.Button(text='Mis ahorros', command=suma_ahorros)
boton2.place(x=203, y=350, width=100, height=40)
boton2.config(background='yellow')

etiqueta_ahorro = tk.Label(text='Historial:')
etiqueta_ahorro.place(x=450, y=20, width=300, height=40)
etiqueta_ahorro.config(background='blue', font=('Arial', 16), fg='white')

lista_ahorros = tk.Label(text='')
lista_ahorros.config(background='white', font=('Arial', 12))
lista_ahorros.place(x=450, y=50, width=300, height=340)

boton3 = tk.Button(text='Historial', command=historial)
boton3.place(x=305, y=350, width=100, height=40)
boton3.config(background='skyblue')

lista_desplegable = tk.Combobox(
 values=[
 "Visual Basic",
 "Python",
 "C",
 "C++",
 "Java"
 ]
)
lista_desplegable.place(x=10, y=10)

ventana.mainloop()