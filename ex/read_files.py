import json
import csv
import os

def read_files(path,files_name):
    for i in files_name:
        if i.split('.')[1] == 'txt':
            with open(path + i, 'r') as file:
                content = file.read()
            print(i)
            print(content)
        if i.split('.')[1] == 'csv':
            with open(path + i, 'r') as file:
                rows = csv.reader(file)
                print(i)
                for row in rows:
                    print(row)
        if i.split('.')[1] == 'json':
            with open(path + i, 'r') as file:
                content = json.load(file)
            print(i)
            print(content)


# read_files('ex/test/',['munte_2023_0.txt','munte_2023_1.txt','munte_2023_2.csv','munte_2023_3.json','munte_2023_4.txt'])


