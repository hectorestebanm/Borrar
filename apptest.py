from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from flask import request
from flask import redirect
app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'bmbbh8qnc5vsvva6pcns-mysql.services.clever-cloud.com'
app.config['MYSQL_DATABASE_USER'] = 'uxhnxwu8dlpq8gxz'
app.config['MYSQL_DATABASE_PASSWORD'] = 'SLPd7DZK7WQVDLYrlieQ'
app.config['MYSQL_DATABASE_BD'] = 'bmbbh8qnc5vsvva6pcns'
mysql.init_app(app)

@app.route("/")
def index():
  sql = "SELECT * FROM `bmbbh8qnc5vsvva6pcns`.`desarrolladores`;"
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(sql)
  db_empleados = cursor.fetchall()
  conn.commit()
  return render_template("empleados/index.html", empleados=db_empleados)

@app.route("/create")
def create():
  return render_template("empleados/create.html")

@app.route("/store", methods=["POST"])
def storage():
  _nombre = request.form["txtNombre"]
  _correo = request.form["txtCorreo"]
  datos = (_nombre, _correo)
  sql = "INSERT INTO `bmbbh8qnc5vsvva6pcns`.`desarrolladores` (`id`, `nombre`, `correo`) VALUES (NULL, %s, %s);"
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(sql, datos)
  conn.commit()
  return redirect("/")

@app.route("/destroy/<int:id>")
def destroy(id):
  sql = "DELETE FROM `bmbbh8qnc5vsvva6pcns`.`desarrolladores` WHERE `desarrolladores`.`id` = %s;"
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(sql,id)
  conn.commit()
  return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
  sql = "SELECT * FROM `bmbbh8qnc5vsvva6pcns`.`desarrolladores` WHERE `desarrolladores`.`id` = %s;"
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(sql,id)
  empleados = cursor.fetchall()
  conn.commit()
  return render_template("empleados/edit.html", empleados=empleados)

@app.route("/update", methods = ["POST"])
def update():
  sql = "UPDATE `bmbbh8qnc5vsvva6pcns`.`desarrolladores` SET `nombre` = %s, `correo` = %s WHERE `desarrolladores`.`id` = %s;"
  _nombre = request.form["txtNombre"]
  _correo = request.form["txtCorreo"]
  _id = request.form["txtID"]
  datos = (_nombre, _correo, _id)
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(sql, datos)
  conn.commit()
  return redirect("/")

if __name__=="__main__":
  app.run(debug=True)
