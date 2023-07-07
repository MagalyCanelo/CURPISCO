from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

from werkzeug.utils import secure_filename
import os

registrar_repuesto = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
}

registrar_repuesto.secret_key = 'mysecretkey'

@registrar_repuesto.route('/')
def index_registrar_repuesto():
    return render_template('RegistrodeRepuestos.html')

@registrar_repuesto.route('/registro_repuesto', methods = ['GET', 'POST'])
def r_registro_repuesto():
    conn = mysql.connector.connect(**db_config)
    if request.method == "POST":
        codigo_repuesto = request.form['codigo_repuesto']
        nombre_repuesto = request.form['nombre_repuesto']
        descripcion_repuesto = request.form['descripcion_repuesto']
        cantidad_minima_repuesto = request.form['cantidad_minima_repuesto']
        foto_repuesto = request.files['foto_repuesto']
        basepath = os.path.dirname(__file__)
        fotonombre = secure_filename(foto_repuesto.filename)
        extension = os.path.splitext(fotonombre)[1]
        nuevo_nombre_foto = nombre_repuesto + extension 
        upload_path = os.path.join (basepath, 'static/imgRepuestos', nuevo_nombre_foto)
        foto_repuesto.save(upload_path)
        cur = conn.cursor()
        cur.execute('INSERT INTO registrar_repuesto (codigo_repuesto, nombre_repuesto, descripcion_repuesto, cantidad_minima_repuesto, foto_repuesto) VALUES (%s, %s, %s, %s, "%s")' , 
                    (codigo_repuesto, nombre_repuesto, descripcion_repuesto, cantidad_minima_repuesto, nuevo_nombre_foto))
        conn.commit()
        
    return redirect(url_for('registrar_repuesto'))

if __name__ == '__main__':
    registrar_repuesto.run(port = 3000, debug = True)
