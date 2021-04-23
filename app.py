from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(

            host='sql10.freemysqlhosting.net',
            database='sql10407298',
            user='sql10407298',
            password='bMthrJ6lsK',)

    except pymysql.Error as e:
        print(e)
    return conn

@app.route("/test", methods=["GET", "POST"])
def test():
    conn = db_connection()
    cursor = conn.cursor()
#Seleccionar
    if request.method == "GET":
        cursor.execute("SELECT * FROM test")
        test = [
            dict(d_estado=row['d_estado'], D_nmpio=row['D_nmpio'],
            d_asenta=roe['d_asenta'], d_CP=row['d_CP'])
            for row in cursor.fetchall()
        ]
        if test is not None:
            return jsonify({'mensaje': 'Bad request'}), 400
#Insertar
    if request.method == "POST":
        new_d_estado = request.form["d_estado"]
        new_D_nmpio = request.form["D_nmpio"]
        new_d_asenta = request.form["d_asenta"]
        new_d_CP = request.form["d_CP"]
        sql = """INSERT INTO test (d_estado, D_nmpio, d_asenta, d_CP) VALUES(%s, %s, %s, %s)"""
        cursor = cursor.execute(sql, (new_d_estado, new_D_nmpio, new_d_asenta, new_d_CP))
        conn.commit()
        return "Se ha agragado nuevo estado, municipio, colonia y codigo postal"
#actualizar
@app.route('/test', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = test.query.get(request.form.get('d_estado, D_nmpio, d_asenta, d_CP'))
  
        my_data.d_estado = request.form['d_estado']
        my_data.D_nmpio = request.form['D_nmpio']
        my_data.d_asenta = request.form['d_asenta']
        my_data.d_CP = request.form['d_CP']

        conn.commit()
        return "Haz actualizado Correctamente"
#Eliminar
@app.route('/test', methods = ['GET', 'POST'])
def delete(d_estado, D_nmpio, d_asenta, d_CP):
    my_data = test.query.get(d_estado)
    my_data = test.query.get(D_nmpio)
    my_data = test.query.get(d_asenta)
    my_data = test.query.get(d_CP)
    conn.delete(my_data)
    conn.commit()
    return "Se ha elmininado"



    
      