from flask import Flask, render_template
import mysql.connector

home = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
}

home.secret_key = 'mysecretkey'

@home.route('/home')
def home_index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM user')
    countAdmi = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM registrar_responsable')
    countResp = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM registrar_proveedor')
    countProv = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM registrar_repuesto')
    countRep = cursor.fetchone()[0]
    
    cursor.close()

    return render_template('home.html', countAdmi=countAdmi, countResp=countResp, countProv=countProv, countRep=countRep)

if __name__ == '__main__':
    home.run(port=3000, debug=True)
