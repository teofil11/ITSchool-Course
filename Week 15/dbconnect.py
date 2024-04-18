from flask import Flask,request
import mysql.connector

app = Flask(__name__)

persons = []

connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'curs')
cursor =  connect.cursor()

@app.route("/")
def home():
    return "Hello world from curs 27!"


@app.route("/persoana", methods=['POST'])
def createPerson():
    data = request.get_json()
    nume = data['nume']
    prenume = data['prenume']
    culoarepar = data['culoare_par']
    porecla = data['porecla']
    cursor.execute(f"insert into persoane values(null,'{nume}','{prenume}','{culoarepar}','{porecla}');")
    connect.commit()
    return 'persoana inserata' + str(cursor.lastrowid)
    

@app.route("/persoana/<id>", methods = ['GET'])
def getPerson(id):
    cursor.execute(f"select * from persoane where id = {id}")
    rows = cursor.fetchall()
    returnable = {}
    for i in range(len(cursor.column_names)):
        returnable[cursor.column_names[i]] = rows[0][i]
    return returnable



@app.route("/persoana/<id>", methods = ['PUT'])
def updatePerson(id):
    data = request.get_json()
    params = {}
    if 'nume' in data:
        params['nume'] = data['nume']
    if 'prenume' in data:
        params['prenume'] = data['prenume']
    if 'culoare_par' in data:
        params['culoare_par'] = data['culoare_par']
    if 'porecla' in data:
        params['porecla'] = data['porecla']
    querry = 'update persoane set '
    for key, value in params.items():
        querry += f"{key}='{value}',"
    querry = querry[:-1]
    querry = f'{querry} where id = {id}' 
    cursor.execute(querry)
    connect.commit()
    return 'updated'



@app.route("/persoana/<id>", methods = ['DELETE'])
def deletePerson(id):
    cursor.execute(f"delete from persoane where id ={id}")
    connect.commit()
    return f'Persoana cu id {id} a fost stearsa cu succes'

if __name__ == '__main__':
    app.run(debug=True)