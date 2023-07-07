from flask import Flask, render_template, jsonify, request, redirect, url_for
import mysql.connector
import base64, json

salida_repuesto = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
} 

class RepuestoManager:
    def __init__(self):
        self.cantidad_actual = None
        self.cantidad_minima_repuesto = None

    def check_stock(self, id_repuesto, cantidad_salida_repuesto):
        advertencia = False  
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos CHECK STOCK")
        else:
            print("No se pudo establecer la conexión a la base de datos")
        cursor = conn.cursor()

        cursor.execute('SELECT cantidad_total, cantidad_minima_repuesto FROM registrar_repuesto WHERE id_repuesto = %s', (id_repuesto,))
        result = cursor.fetchone()

        if result:
            self.cantidad_actual, self.cantidad_minima_repuesto = result
            if self.cantidad_actual >= cantidad_salida_repuesto:
                nueva_cantidad = self.cantidad_actual - cantidad_salida_repuesto
                if nueva_cantidad <= self.cantidad_minima_repuesto:
                    advertencia = True
                    mensaje_advertencia = "Advertencia: La cantidad de repuesto es igual o menor que la cantidad mínima."
                else:
                    advertencia = False
                cursor.execute('UPDATE registrar_repuesto SET cantidad_total = %s WHERE id_repuesto = %s', (nueva_cantidad, id_repuesto))
                conn.commit()
                if advertencia:
                    print(mensaje_advertencia)
        else:
            print("Error: La cantidad solicitada es mayor que la cantidad disponible en stock.")

        cursor.close()
        conn.close()

        if advertencia:
            mensaje_advertencia = "Advertencia: La cantidad de repuesto es igual o menor que la cantidad mínima."
            return advertencia, mensaje_advertencia
        else:
            return advertencia, None

repuesto_manager = RepuestoManager()

@salida_repuesto.route('/obtener_cantidades', methods=['POST'])
def index_obtener_cantidades():
    if request.method == 'POST':
        data = request.get_json()
        codigo_repuesto = data.get('codigo_repuesto')

        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos CHECK STOCK")
        else:
            print("No se pudo establecer la conexión a la base de datos")
        cursor = conn.cursor()
        
        cursor.execute('SELECT id_repuesto FROM registrar_repuesto WHERE codigo_repuesto = %s', (codigo_repuesto,))
        id_repuesto = cursor.fetchone()    
        id_repuesto = id_repuesto[0] 

        cursor.execute('SELECT cantidad_total, cantidad_minima_repuesto FROM registrar_repuesto WHERE id_repuesto = %s', (id_repuesto,))
        db_data = cursor.fetchone()
        
        cantidad_actual = db_data[0]  
        cantidad_minima_repuesto = db_data[1] 
        data = {
            'cantidad_actual': cantidad_actual,
            'cantidad_minima_repuesto': cantidad_minima_repuesto
        }
        
        json_data = json.dumps(data)
    
    return json_data

@salida_repuesto.route('/registrar_salida')
def index_salida_repuesto():
    response_data = {} 
    return render_template('SalidadeRepuestos.html', cantidad_actual=repuesto_manager.cantidad_actual, cantidad_minima_repuesto=repuesto_manager.cantidad_minima_repuesto, data=response_data)

@salida_repuesto.route('/autocompletar_salida', methods=['GET', 'POST'])
def autocompletar_repuesto_salida():
    codigo_repuesto = request.form.get('codigo_repuesto')

    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexión exitosa a la base de datos AUTO SALIDA")
    else:
        print("No se pudo establecer la conexión a la base de datos")
        return jsonify({'data': {}})
    cursor = conn.cursor()

    query = "SELECT nombre_repuesto, descripcion_repuesto, foto_repuesto FROM registrar_repuesto WHERE codigo_repuesto = %s"
    cursor.execute(query, (codigo_repuesto,))
    result = cursor.fetchone()

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

@salida_repuesto.route('/autocompletar_responsable', methods=['GET', 'POST'])
def autocompletar_responsable_salida():
    codigo_responsable = request.form.get('codigo_responsable')

    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexión exitosa a la base de datos AUTO RESPONSABLE")
    else:
        print("No se pudo establecer la conexión a la base de datos")
        return jsonify({'data': {}}) 

    cursor = conn.cursor()
    query = "SELECT nombres_responsable, apellidos_responsable FROM registrar_responsable WHERE codigo_responsable = %s"
    cursor.execute(query, (codigo_responsable,))
    result = cursor.fetchone()
    print("Result es:", result)

    cursor.close()
    conn.close()

    data = {
        'nombres_responsable': result[0],
        'apellidos_responsable': result[1]
    }

    return jsonify({'data': data})

@salida_repuesto.route('/registro_salida', methods=['GET', 'POST'])
def r_registro_salida():
    if request.method == "POST":
        codigo_repuesto = request.form['codigo_repuesto']
        cantidad_salida_repuesto = request.form['cantidad_salida_repuesto']
        codigo_responsable = request.form['codigo_responsable']
        fecha_salida_repuesto = request.form['fecha_salida_repuesto']

        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos REGISTRO")
        else:
            print("No se pudo establecer la conexión a la base de datos")
        response_data = {}

        cur = conn.cursor()
        cur.execute('SELECT id_repuesto, cantidad_total, cantidad_minima_repuesto FROM registrar_repuesto WHERE codigo_repuesto = %s', (codigo_repuesto,))
        result = cur.fetchone()
        cur.execute('SELECT id_responsable FROM registrar_responsable WHERE codigo_responsable = %s', (codigo_responsable,))
        id_responsable = cur.fetchone()    
        id_responsable = id_responsable[0] 

        if result:
            id_repuesto, cantidad_actual, cantidad_minima_repuesto = result
            advertencia, mensaje_advertencia = repuesto_manager.check_stock(id_repuesto, int(cantidad_salida_repuesto))

        cur.execute('INSERT INTO salida_repuesto (id_repuesto, cantidad_salida_repuesto, id_responsable, fecha_salida_repuesto) VALUES (%s, %s, %s, %s)',
                    (id_repuesto, cantidad_salida_repuesto, id_responsable, fecha_salida_repuesto))

        conn.commit()

        cur.close()
        conn.close()

        return render_template('SalidadeRepuestos.html', data=response_data)

    return redirect(url_for('salida_repuesto'), cantidad_actual=repuesto_manager.cantidad_actual, cantidad_minima_repuesto=repuesto_manager.cantidad_minima_repuesto)

if __name__ == '__main__':
    salida_repuesto.run(port=3000, debug=True)