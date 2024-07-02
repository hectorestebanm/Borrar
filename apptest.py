from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from flask import request
from flask import redirect
app=Flask(__name__)

# mysql = MySQL()
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_BD'] = 'mibasededatos'
# mysql.init_app(app)

@app.route("/")
def index():
  # sql = "SELECT * FROM `mibasededatos`.`miTabla`;"
  # conn = mysql.connect()
  # cursor = conn.cursor()
  # cursor.execute(sql)
  # db_empleados = cursor.fetchall()
  # conn.commit()
  return render_template("empleados/index.html")

@app.route("/create")
def create():
  return render_template("empleados/create.html")

@app.route("/store", methods=["POST"])
def storage():
  _nombre = request.form["txtNombre"]
  _correo = request.form["txtCorreo"]
  datos = (_nombre, _correo)
  # sql = "INSERT INTO `mibasededatos`.`miTabla` (`id`, `nombre`, `email`) VALUES (NULL, %s, %s);"
  # conn = mysql.connect()
  # cursor = conn.cursor()
  # cursor.execute(sql, datos)
  # conn.commit()
  return redirect("/")

@app.route("/destroy/<int:id>")
def destroy(id):
  # sql = "DELETE FROM `mibasededatos`.`miTabla` WHERE `miTabla`.`id` = %s;"
  # conn = mysql.connect()
  # cursor = conn.cursor()
  # cursor.execute(sql,id)
  # conn.commit()
  return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
  # sql = "SELECT * FROM `mibasededatos`.`miTabla` WHERE `miTabla`.`id` = %s;"
  # conn = mysql.connect()
  # cursor = conn.cursor()
  # cursor.execute(sql,id)
  # empleados = cursor.fetchall()
  # conn.commit()
  return render_template("empleados/edit.html")

@app.route("/update", methods = ["POST"])
def update():
  # sql = "UPDATE `mibasededatos`.`miTabla` SET `nombre` = %s, `email` = %s WHERE `miTabla`.`id` = %s;"
  _nombre = request.form["txtNombre"]
  _correo = request.form["txtCorreo"]
  id = request.form["txtID"]
  datos = (_nombre, _correo, id)
  # conn = mysql.connect()
  # cursor = conn.cursor()
  # cursor.execute(sql, datos)
  # conn.commit()
  return redirect("/")

if __name__=="__main__":
  app.run(debug=True)
