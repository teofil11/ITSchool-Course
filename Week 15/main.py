from flask import Flask,request,jsonify
import json

app = Flask(__name__)

persons = []

@app.route("/")
def home():
    return "Hello world!"


@app.route("/person/", methods= ['POST'])
def postPerson():
    data = request.get_json()
    data['id'] = len(persons)
    persons.append(data)
    print(persons)
    return 'Am procesat persoana'


@app.route("/person/<id>", methods= ['GET'])
def getFunction(id):
    for person in persons:
        if str(id) == str(person['id']):
            return person
    return 'Nu am gasit persoane'


@app.route("/person/<id>", methods=['PUT'])
def updatePerson(id):
    for person in persons:
        if str(id) == str(person['id']):
            person["nume"]= "Teodorescu"
            person["prenume"]= "Teofil"
            return person
    return 'Nu am gasit persoane'


@app.route("/person/<id>", methods=['DELETE'])
def deletePerson(id):
    global persons
    continut = []
    for person in persons:
        if str(id) != str(person['id']):
            continut.append(person)
    persons = continut
    return 'Persoana stearsa'

if __name__ == '__main__':
    app.run(debug=True)


