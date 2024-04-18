import json
import random


# am folosit acest script pentru a genera fisierul employees.json
positions = ["Manager", "Developer", "Salesperson", "Designer"]
employees = []

for i in range(1, 101):
    name = f"Employee {i}"
    position = random.choice(positions)
    salary = random.randint(30000, 100000)
    employee = {"id": i, "name": name, "position": position, "salary": salary}
    employees.append(employee)
    

with open('curs15/employees.json','w') as file:
    json.dump(employees,file)
