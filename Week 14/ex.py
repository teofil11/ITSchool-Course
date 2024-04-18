import requests
import json

def get_temperature(latitude, longitude):
    URL=f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=3&timezone=auto'
    r=requests.get(url=URL)
    data=r.json()
    times = data['hourly']['time']
    temperatures = data['hourly']['temperature_2m']
    for  i,time in enumerate(times):
        print(time+' - '+str(temperatures[i]))
# get_temperature(46.38314760247552, 23.76598923259678)


def medium_temoerature(latitude, longitude):
    URL = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=3&timezone=auto'
    response = requests.get(URL)
    data = response.json()
    times = data['hourly']['time']
    temperatures = data['hourly']['temperature_2m']
    ziua1 = 0
    ziua2 = 0
    ziua3 = 0
    for i in range(24):
        ziua1 += temperatures[i]
    for i in range(24,48):
        ziua2 += temperatures[i]
    for i in range(48,72):
        ziua3 += temperatures[i]
    print(f'Pentru ziua 1  media este de {ziua1/24}')
    print(f'Pentru ziua 2  media este de {ziua2/24}')
    print(f'Pentru ziua 3  media este de {ziua3/24}')

# medium_temoerature(46.38314760247552, 23.76598923259678)

def create_user(nume,prenume):
    URL = "http://92.86.61.172:5000/person"
    data = {'nume': nume,'prenume': prenume}
    json_data = json.dumps(data)
    params = {'Content-Type': 'application/json', 'Accept': '*/*'}
    response = requests.post(URL,data = json_data, headers=params)
    print(response)

# create_user('Teodorescu', 'Teofil')

def get_user():
    URL = "http://92.86.61.172:5000/person/1"
    response = requests.get(URL)
    data = response.text  
    print(data)

# get_user()

def update_user(id):
    URL = "http://92.86.61.172:5000/person/" +str(id)
    data = {'nume': 'ucserodoet','prenume': 'Teofil'}
    params = {'Content-Type': 'application/json', 'Accept': '*/*'}
    json_data = json.dumps(data)
    r = requests.put(URL, data=json_data,headers=params)
    print(r.text)
    
# update_user(1)

def delete_user(id):
    URL = "http://92.86.61.172:5000/person/" +str(id)
    r = requests.delete(URL)
    print(r.text) 

# delete_user(1)


def translate(text,source_language,target_language):
    URL = f"https://api.mymemory.translated.net/get?q={text}&langpair={source_language}|{target_language}"
    r = requests.get(URL)
    translate = r.json()['responseData']['translatedText']
    print(translate)

translate("salut",'ro','en')




    





