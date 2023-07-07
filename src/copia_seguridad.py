from flask import Flask, send_file
import mysql.connector
import os
from datetime import datetime

copia_seguridad = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'curpiscobd_repuesto'
}

def generar_copia_de_seguridad():
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"copiaDeSeguridad_{fecha_actual}.sql"
    ruta_carpeta = os.path.join(copia_seguridad.static_folder, 'copiaDeSeguridad')
    ruta_copia_seguridad = os.path.join(ruta_carpeta, nombre_archivo)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    with open(ruta_copia_seguridad, 'w') as archivo:
        for tabla in tablas:
            tabla = tabla[0]
            cursor.execute(f"SELECT * FROM {tabla}")
            resultados = cursor.fetchall()

            cursor.execute(f"SHOW CREATE TABLE {tabla}")
            create_table_statement = cursor.fetchone()[1]
            archivo.write(f"{create_table_statement};\n\n")

            for resultado in resultados:
                archivo.write(f"INSERT INTO {tabla} VALUES {str(resultado)};\n")

            archivo.write("\n")

    cursor.close()
    conn.close()

@copia_seguridad.route('/generar_copia_de_seguridad', methods=['POST'])
def ruta_generar_copia_de_seguridad():
    generar_copia_de_seguridad()
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"copiaDeSeguridad_{fecha_actual}.sql"
    ruta_archivo = os.path.join(copia_seguridad.static_folder, 'copiaDeSeguridad', nombre_archivo)
    return send_file(ruta_archivo, as_attachment=True)

if __name__ == '__main__':
    copia_seguridad.run()
