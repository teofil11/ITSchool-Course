import mysql.connector
import csv


conn = mysql.connector.connect(host='localhost',user='root', password='root', database='curs')
cursor = conn.cursor()
cursor.execute("select * from clase")
rows = cursor.fetchall()

# for row in rows:
#     print(row)

def insert_persoana():
    nume = input('Introduceti numele:')
    prenume = input('Introduceti prenume:')
    culoare_par = input('Culoare par:')
    porecla = input('Porecla:')
    cursor.execute(f"insert into persoane values (null,'{nume}','{prenume}','{culoare_par}','{porecla}');")
    conn.commit()

def sterge_persoana():
    cursor.execute("delete from persoane where culoare_par = 'blond'")
    conn.commit()

def adauga_in_clasa():
    cursor.execute("select * from clase")
    rows = cursor.fetchall()
    for row in rows:
        print(f'Clasa {row[1]}: {row}')
    nume = input('Introduceti numele:')
    prenume = input('Introduceti prenume:')
    culoare_par = input('Culoare par:')
    porecla = input('Porecla:')
    clasa = int(input('Alege clasa: '))
    cursor.execute(f"insert into persoana_clasa values (null,'{nume}','{prenume}','{culoare_par}','{porecla}');")
    conn.commit()
    cursor.execute("select id from persoane;")
    id = cursor.fetchall()
    last_id = id[-1]
    x = list(last_id)
    cursor.execute(f"insert into persoana_clasa values({x},{clasa});")
    conn.commit()

def functie():
    with open("Week 13/employees.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(f"insert into persoane values(null,'{row[1]}','{row[2]}','brunet','{row[3]}');")
        conn.commit()




conn.close()
cursor.close()