from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

registrar_proveedor = Flask(__name__)

registrar_proveedor.config['MYSQL_HOST'] = 'localhost'
registrar_proveedor.config['MYSQL_USER'] = 'root'
registrar_proveedor.config['MYSQL_PASSWORD'] = ''
registrar_proveedor.config['MYSQL_DB'] = 'curpiscobd_repuesto'
mysql = MySQL(registrar_proveedor)

registrar_proveedor.secret_key = 'mysecretkey'

@registrar_proveedor.route('/')
def index_registrar_proveedor():
    return render_template('RegistrodeProveedores.html')

@registrar_proveedor.route('/registro_proveedor', methods = ['GET', 'POST'])
def r_registro_proveedor():
    if request.method == "POST":
        codigo_proveedor = request.form['codigo_proveedor']
        ruc_proveedor = request.form['ruc_proveedor']
        razon_social_proveedor = request.form['razon_social_proveedor']
        telefono_proveedor = request.form['telefono_proveedor']
        direccion_proveedor = request.form['direccion_proveedor']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO registrar_proveedor (codigo_proveedor, ruc_proveedor, razon_social_proveedor, telefono_proveedor, direccion_proveedor) VALUES (%s, %s, %s, %s, %s)' , 
                    (codigo_proveedor, ruc_proveedor, razon_social_proveedor, telefono_proveedor, direccion_proveedor))
        mysql.connection.commit()
        
    return redirect(url_for('registrar_proveedor'))

if __name__ == '__main__':
    registrar_proveedor.run(port = 3000, debug = True)
