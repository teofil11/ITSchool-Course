from flask import Flask, render_template,request
import mysql.connector


app = Flask(__name__)
number = "7"

connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'contact')
cursor =  connect.cursor()


@app.route('/person', methods = ['POST'])
def insert_person():
    data = request.get_json()
    print(data)
    return 'Datele au fost procesate'

if __name__ == '__main__':
    app.run(debug=True)