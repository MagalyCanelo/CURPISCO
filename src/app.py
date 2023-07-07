from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

from home import home_index
from copia_seguridad import ruta_generar_copia_de_seguridad 
from registrar_usuario import crear_cuenta_index, r_registro_usuario
from registrar_repuesto import index_registrar_repuesto, r_registro_repuesto
from entrada_repuesto import index_entrada_repuesto, autocompletar_repuesto_entrada, autocompletar_proveedor_entrada, r_registro_entrada
from salida_repuesto import index_salida_repuesto, autocompletar_repuesto_salida, autocompletar_responsable_salida, index_obtener_cantidades, r_registro_salida
from registrar_proveedor import index_registrar_proveedor, r_registro_proveedor
from registrar_responsable import index_registrar_responsable, r_registro_responsable
from mostrar_inventario import index_mostrar_inventario, index_limpiar_filtro, index_buscar_repuesto, index_edit_inventario, index_update_repuesto, index_delete_repuesto, index_generar_excel
from mostrar_entrada import index_mostrar_entrada, index_limpiar_filtroE, index_buscar_entrada, index_edit_entrada, autocompletar_repuesto_entradaE, autocompletar_proveedor_entradaE, index_update_entrada, index_delete_entrada, index_generar_excelE
from mostrar_salida import index_mostrar_salida, index_limpiar_filtroS, index_buscar_salida, index_edit_salida, autocompletar_repuesto_salidaS, autocompletar_responsable_salidaS, index_update_salida, index_delete_salida, index_generar_excelS
from mostrar_proveedores import index_mostrar_proveedor, index_limpiar_filtroP, index_buscar_proveedor, index_edit_proveedor, index_update_proveedor, index_delete_proveedor, index_generar_excelP
from mostrar_responsables import index_mostrar_responsable, index_limpiar_filtroR, index_buscar_responsable, index_edit_responsable, index_update_responsable, index_delete_responsable, index_generar_excelR

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

csrf = CSRFProtect(app)
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'crear_cuenta' in request.form:
            return redirect(url_for('crear_cuenta'))
                        
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña Incorrecta")
                return render_template('inicioSesion.html')
        else:
            flash("Usuario No Encontrado") 
            return render_template('inicioSesion.html')
    else:
        return render_template('inicioSesion.html')
        
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return home_index()

@app.route('/generar_copia_de_seguridad', methods=['POST'])
@csrf.exempt
def generar_copia_de_seguridad():
    csrf_token = generate_csrf()
    return ruta_generar_copia_de_seguridad()

@app.route('/crear_cuenta')
def crear_cuenta():
    return crear_cuenta_index()

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    return r_registro_usuario()

# REPUESTO
@app.route('/registrar_repuesto')
def registrar_repuesto():
    return index_registrar_repuesto()

@app.route('/registro_repuesto', methods=['GET', 'POST'])
def registro_repuesto():
    return r_registro_repuesto()

# ENTRADA 
@app.route('/entrada_repuesto')
def entrada_repuesto():
    return index_entrada_repuesto()

@app.route('/autocompletar_entrada', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_entrada():
    csrf_token = generate_csrf()
    return autocompletar_repuesto_entrada()

@app.route('/autocompletar_proveedor', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_proveedor():
    csrf_token = generate_csrf()
    return autocompletar_proveedor_entrada()

@app.route('/registro_entrada', methods=['GET', 'POST'])
@csrf.exempt
def registro_entrada():
    csrf_token = generate_csrf()
    return r_registro_entrada()

# SALIDA
@app.route('/salida_repuesto')
def salida_repuesto():
    return index_salida_repuesto()

@app.route('/autocompletar_salida', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_salida():
    csrf_token = generate_csrf()
    return autocompletar_repuesto_salida()

@app.route('/autocompletar_responsable', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_responsable():
    csrf_token = generate_csrf()
    return autocompletar_responsable_salida()

@app.route('/obtener_cantidades', methods=['POST'])
@csrf.exempt
def obtener_cantidades():
    csrf_token = generate_csrf()
    return index_obtener_cantidades()

@app.route('/registro_salida', methods=['GET', 'POST'])
@csrf.exempt
def registro_salida():
    csrf_token = generate_csrf()
    return r_registro_salida()

# MOSTRAR INVENTARIO
@app.route('/mostrar_inventario')
def mostrar_inventario():
    return index_mostrar_inventario()

@app.route('/limpiar_filtro', methods=['GET'])
@csrf.exempt
def limpiar_filtro():
    csrf_token = generate_csrf()
    return index_limpiar_filtro()

@app.route('/buscar_repuesto', methods=['POST'])
@csrf.exempt
def buscar_repuesto():
    csrf_token = generate_csrf()
    return index_buscar_repuesto()

@app.route('/edit_inventario/<id>')
def edit_inventario(id):
    return index_edit_inventario(id)

@app.route('/update_repuesto/<id>', methods=['POST'])
@csrf.exempt
def update_repuesto(id):
    csrf_token = generate_csrf()
    return index_update_repuesto(id)

@app.route('/delete_inventario/<string:id>', methods=['GET', 'POST'])
@csrf.exempt
def delete_repuesto(id):
    csrf_token = generate_csrf()
    return index_delete_repuesto(id)

@app.route('/generar_excel', methods=['POST'])
@csrf.exempt
def generar_excel():
    csrf_token = generate_csrf()
    return index_generar_excel()

# MOSTRAR ENTRADA
@app.route('/mostrar_entrada')
def mostrar_entrada():
    return index_mostrar_entrada()

@app.route('/limpiar_filtroE', methods=['GET'])
@csrf.exempt
def limpiar_filtroE():
    csrf_token = generate_csrf()
    return index_limpiar_filtroE()

@app.route('/buscar_entrada', methods=['POST'])
@csrf.exempt
def buscar_entrada():
    csrf_token = generate_csrf()
    return index_buscar_entrada()

@app.route('/edit_entrada/<id>') 
def edit_entrada(id):
    return index_edit_entrada(id)

@app.route('/autocompletar_entradaE', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_entradaE():
    csrf_token = generate_csrf()
    return autocompletar_repuesto_entradaE()

@app.route('/autocompletar_proveedorE', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_proveedorE():
    csrf_token = generate_csrf()
    return autocompletar_proveedor_entradaE()

@app.route('/update_entrada/<id>', methods=['POST']) 
@csrf.exempt
def update_entrada(id):
    csrf_token = generate_csrf()
    return index_update_entrada(id)

@app.route('/delete_entrada/<string:id>', methods=['GET', 'POST']) 
@csrf.exempt
def delete_entrada(id):
    csrf_token = generate_csrf()
    return index_delete_entrada(id)

@app.route('/generar_excelE', methods=['POST']) 
@csrf.exempt
def generar_excelE():
    csrf_token = generate_csrf()
    return index_generar_excelE()

# MOSTRAR SALIDA
@app.route('/mostrar_salida')
def mostrar_salida():
    return index_mostrar_salida()

@app.route('/limpiar_filtroS', methods=['GET'])
@csrf.exempt
def limpiar_filtroS():
    csrf_token = generate_csrf()
    return index_limpiar_filtroS()

@app.route('/buscar_salida', methods=['POST'])
@csrf.exempt
def buscar_salida():
    csrf_token = generate_csrf()
    return index_buscar_salida()

@app.route('/edit_salida/<id>')
def edit_salida(id):
    return index_edit_salida(id)

@app.route('/autocompletar_salidaS', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_salidaS():
    csrf_token = generate_csrf()
    return autocompletar_repuesto_salidaS()

@app.route('/autocompletar_responsableS', methods=['GET', 'POST'])
@csrf.exempt
def autocompletar_responsableS():
    csrf_token = generate_csrf()
    return autocompletar_responsable_salidaS()

@app.route('/update_salida/<id>', methods=['POST']) 
@csrf.exempt
def update_salida(id):
    csrf_token = generate_csrf()
    return index_update_salida(id)

@app.route('/delete_salida/<string:id>', methods=['GET', 'POST']) 
@csrf.exempt
def delete_salida(id):
    csrf_token = generate_csrf()
    return index_delete_salida(id)

@app.route('/generar_excelS', methods=['POST']) 
@csrf.exempt
def generar_excelS():
    csrf_token = generate_csrf()
    return index_generar_excelS()

# PROVEEDOR
@app.route('/registrar_proveedor')
def registrar_proveedor():
    return index_registrar_proveedor()

@app.route('/registro_proveedor', methods=['GET', 'POST'])
def registro_proveedor():
    return r_registro_proveedor()

# MOSTRAR PROVEEDOR
@app.route('/mostrar_proveedor')
def mostrar_proveedor():
    return index_mostrar_proveedor()

@app.route('/limpiar_filtroP', methods=['GET'])
@csrf.exempt
def limpiar_filtroP():
    csrf_token = generate_csrf()
    return index_limpiar_filtroP()

@app.route('/buscar_proveedor', methods=['POST'])
@csrf.exempt
def buscar_proveedor():
    csrf_token = generate_csrf()
    return index_buscar_proveedor()

@app.route('/edit_proveedor/<id>')
def edit_proveedor(id):
    return index_edit_proveedor(id)

@app.route('/update_proveedor/<id>', methods=['POST'])
@csrf.exempt
def update_proveedor(id):
    csrf_token = generate_csrf()
    return index_update_proveedor(id)

@app.route('/delete_proveedor/<string:id>', methods=['GET', 'POST'])
@csrf.exempt
def delete_proveedor(id):
    csrf_token = generate_csrf()
    return index_delete_proveedor(id)

@app.route('/generar_excelP', methods=['POST'])
@csrf.exempt
def generar_excelP():
    csrf_token = generate_csrf()
    return index_generar_excelP()

# RESPONSABLE
@app.route('/registrar_responsable')
def registrar_responsable():
    return index_registrar_responsable()

@app.route('/registro_responsable', methods=['GET', 'POST'])
def registro_responsable():
    return r_registro_responsable()

# MOSTRAR RESPONSABLE
@app.route('/mostrar_responsable')
def mostrar_responsable():
    return index_mostrar_responsable()

@app.route('/limpiar_filtroR', methods=['GET'])
@csrf.exempt
def limpiar_filtroR():
    csrf_token = generate_csrf()
    return index_limpiar_filtroR()

@app.route('/buscar_responsable', methods=['POST'])
@csrf.exempt
def buscar_responsable():
    csrf_token = generate_csrf()
    return index_buscar_responsable()

@app.route('/edit_responsable/<id>')
def edit_responsable(id):
    return index_edit_responsable(id)

@app.route('/update_responsable/<id>', methods=['POST'])
@csrf.exempt
def update_responsable(id):
    csrf_token = generate_csrf()
    return index_update_responsable(id)

@app.route('/delete_responsable/<string:id>', methods=['GET', 'POST'])
@csrf.exempt
def delete_responsable(id):
    csrf_token = generate_csrf()
    return index_delete_responsable(id)

@app.route('/generar_excelR', methods=['POST'])
@csrf.exempt
def generar_excelR():
    csrf_token = generate_csrf()
    return index_generar_excelR()

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port=3000, debug=True)
    