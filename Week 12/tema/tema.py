date = {
    'masini':[
        {'marca': 'Audi', 'an_fabricatie': 2017, 'combustibil': 'motorina', 'culoare': 'alb', 'nr_km': 43000},
        {'marca': 'BMW', 'an_fabricatie': 2019, 'combustibil': 'benzina', 'culoare': 'gri', 'nr_km': 30000},
        {'marca': 'Mercedes', 'an_fabricatie': 2022, 'combustibil': 'electric', 'culoare': 'negru', 'nr_km': 10000},
        {'marca': 'Dacia', 'an_fabricatie': 2007, 'combustibil': 'benzina', 'culoare': 'albastru', 'nr_km': 310000},
        {'marca': 'Skoda', 'an_fabricatie': 2009, 'combustibil': 'motorina', 'culoare': 'alb', 'nr_km': 245000},
        {'marca': 'Ford', 'an_fabricatie': 2010, 'combustibil': 'benzina', 'culoare': 'albastru', 'nr_km': 210000}
    ],
    'service': [
        {'oras': 'Bucuresti', 'nume': 'Service1'},
        {'oras': 'Cluj Napoca', 'nume': 'Service2'},
        {'oras': 'Bucuresti', 'nume': 'Service3'},
        {'oras': 'Timisoara', 'nume': 'Service4'}
    ],
    'reparatii': [
        {'id_masina': 1, 'id_service': 3, 'tip_interventie': 'revizie'},
        {'id_masina': 4, 'id_service': 2, 'tip_interventie': 'reparatie motor'},
        {'id_masina': 2, 'id_service': 4, 'tip_interventie': 'revizie'},
        {'id_masina': 6, 'id_service': 1, 'tip_interventie': 'reparatie motor'},
        {'id_masina': 5, 'id_service': 3, 'tip_interventie': 'reparatie turbina'}
    ]
}


def genereaza_insert(data):
    for masina in data['masini']:
        insert = f"INSERT INTO masini VALUES(null, '{masina['marca']}', {masina['an_fabricatie']}, '{masina['combustibil']}', '{masina['culoare']}', {masina['nr_km']});"
        print(insert)

    for service in data['service']:
        insert = f"INSERT INTO service VALUES(null, '{service['oras']}', '{service['nume']}');"
        print(insert)

    for reparatie in data['reparatii']:
        insert = f"INSERT INTO reparatii VALUES(null, {reparatie['id_masina']}, {reparatie['id_service']}, '{reparatie['tip_interventie']}');"
        print(insert)


genereaza_insert(date)

