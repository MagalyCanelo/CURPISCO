from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash

registrar_responsable = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
}

registrar_responsable.secret_key = 'mysecretkey'

@registrar_responsable.route('/crear_cuenta')
def crear_cuenta_index():
    return render_template('RegistroCuenta.html')

@registrar_responsable.route('/registro_usuario', methods=['GET', 'POST'])
def r_registro_usuario():
    conn = mysql.connector.connect(**db_config)

    if request.method == "POST":
        username = request.form['username']
        password_plana = request.form['password_hash']
        password_hash = generate_password_hash(password_plana)
        fullname = request.form['fullname']
        cur = conn.cursor()
        cur.execute('INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s)',
                    (username, password_hash, fullname))
        conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    registrar_responsable.run(port = 3000, debug = True)
