from flask import Flask, render_template, jsonify, request, redirect, url_for
import mysql.connector
import base64

entrada_repuesto = Flask(__name__)


db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
}

@entrada_repuesto.route('/registrar_entrada')
def index_entrada_repuesto():
    response_data = {} 
    return render_template('EntradadeRepuestos.html', data=response_data)

@entrada_repuesto.route('/autocompletar_entrada', methods=['GET', 'POST'])
def autocompletar_repuesto_entrada():
    codigo_repuesto = request.form.get('codigo_repuesto')

    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexión exitosa a la base de datos")
    else:
        print("No se pudo establecer la conexión a la base de datos")
        return jsonify({'data': {}})
    cursor = conn.cursor()

    query = "SELECT nombre_repuesto, descripcion_repuesto, foto_repuesto FROM registrar_repuesto WHERE codigo_repuesto = %s"
    cursor.execute(query, (codigo_repuesto,))
    result = cursor.fetchone()
    print("Result es:", result)

    if result:
        nombre_repuesto, descripcion_repuesto, foto_repuesto = result

        if foto_repuesto is not None:
            foto_repuesto_encoded = base64.b64encode(foto_repuesto).decode('ascii')
        else:
            foto_repuesto_encoded = None

        response_data = {
            'nombre_repuesto': nombre_repuesto,
            'descripcion_repuesto': descripcion_repuesto,
            'foto_repuesto': foto_repuesto_encoded
        }
    else:
        response_data = {}

    cursor.close()
    conn.close()

    return jsonify({'data': response_data})

@entrada_repuesto.route('/autocompletar_proveedor', methods=['GET', 'POST'])
def autocompletar_proveedor_entrada():
    codigo_proveedor = request.form.get('codigo_proveedor')

    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexión exitosa a la base de datos")
    else:
        print("No se pudo establecer la conexión a la base de datos")
        return jsonify({'data': {}}) 

    cursor = conn.cursor()
    query = "SELECT razon_social_proveedor FROM registrar_proveedor WHERE codigo_proveedor = %s"
    cursor.execute(query, (codigo_proveedor,))
    result = cursor.fetchone()
    print("Result es:", result)

    cursor.close()
    conn.close()

    return jsonify({'data': result[0]})

@entrada_repuesto.route('/registro_entrada', methods=['GET', 'POST'])
def r_registro_entrada():
    if request.method == "POST":
        codigo_repuesto = request.form['codigo_repuesto']
        cantidad_entrada_repuesto = int(request.form['cantidad_entrada_repuesto'])
        codigo_proveedor = request.form['codigo_proveedor']
        fecha_entrada_repuesto = request.form['fecha_entrada_repuesto']
        
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
        else:
            print("No se pudo establecer la conexión a la base de datos")
        cur = conn.cursor()
        
        cur.execute('SELECT id_repuesto FROM registrar_repuesto WHERE codigo_repuesto = %s', (codigo_repuesto,))
        id_repuesto = cur.fetchone()    
        id_repuesto = id_repuesto[0] 
        cur.execute('SELECT id_proveedor FROM registrar_proveedor WHERE codigo_proveedor = %s', (codigo_proveedor,))
        id_proveedor = cur.fetchone()    
        id_proveedor = id_proveedor[0] 
        
        cur.execute('SELECT cantidad_total FROM registrar_repuesto WHERE id_repuesto = %s', (id_repuesto,))
        result = cur.fetchone()
        
        if result:
            cantidad_actual = result[0]
            nueva_cantidad = cantidad_actual + cantidad_entrada_repuesto
            cur.execute('UPDATE registrar_repuesto SET cantidad_total = %s WHERE id_repuesto = %s',
            (nueva_cantidad, id_repuesto))
            cur.execute('INSERT INTO entrada_repuesto (id_repuesto, cantidad_entrada_repuesto, id_proveedor, fecha_entrada_repuesto) VALUES (%s, %s, %s, %s)',
            (id_repuesto, cantidad_entrada_repuesto, id_proveedor, fecha_entrada_repuesto))
            
        conn.commit()
        
        cur.close()
        conn.close()
        
    return redirect(url_for('entrada_repuesto'))

if __name__ == '__main__':
    entrada_repuesto.run(port = 3000, debug = True)
