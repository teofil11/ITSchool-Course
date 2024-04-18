from flask import Flask, render_template,request
import mysql.connector


app = Flask(__name__)
number = "7"

connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'contact')
cursor =  connect.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person', methods = ['POST'])
def insert_person():
    data = request.get_json()
    nume = data['name']
    email = data['email']
    mesaj = data['message']
    cursor.execute(f"insert into contacte values(null,'{nume}','{email}','{mesaj}')")
    connect.commit()
    return 'Datele au fost procesate'

if __name__ == '__main__':
    app.run(debug=True)