from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

registrar_responsable = Flask(__name__)

registrar_responsable.config['MYSQL_HOST'] = 'localhost'
registrar_responsable.config['MYSQL_USER'] = 'root'
registrar_responsable.config['MYSQL_PASSWORD'] = ''
registrar_responsable.config['MYSQL_DB'] = 'curpiscobd_repuesto'
mysql = MySQL(registrar_responsable)

registrar_responsable.secret_key = 'mysecretkey'

@registrar_responsable.route('/')
def index_registrar_responsable():
    return render_template('RegistrodeResponsables.html')

@registrar_responsable.route('/registro_responsable', methods = ['GET', 'POST'])
def r_registro_responsable():
    if request.method == "POST":
        codigo_responsable = request.form['codigo_responsable']
        nombres_responsable = request.form['nombres_responsable']
        apellidos_responsable = request.form['apellidos_responsable']
        telefono_responsable = request.form['telefono_responsable']
        direccion_responsable = request.form['direccion_responsable']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO registrar_responsable (codigo_responsable, nombres_responsable, apellidos_responsable, telefono_responsable, direccion_responsable) VALUES (%s, %s, %s, %s, %s)' , 
                    (codigo_responsable, nombres_responsable, apellidos_responsable, telefono_responsable, direccion_responsable))
        mysql.connection.commit()
        
    return redirect(url_for('registrar_responsable'))

if __name__ == '__main__':
    registrar_responsable.run(port = 3000, debug = True)
