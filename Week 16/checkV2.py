import datetime
import random
import time
import requests
import json



def main():
    URL = 'http://127.0.0.1:5000/gate'
    persoane=[]
    while(True):
        alegere=random.randint(0,1)
        output={
                "data":datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
                "idPoarta":random.randint(1,3)

            }
        aIntrat=False
        if(alegere==1):
            #intrare
            
            idPersoana=random.randint(1,30)
            while(idPersoana in persoane):
                idPersoana=random.randint(1,30)
            output["sens"]="in"
            output["idPersoana"]=idPersoana
            persoane.append(output['idPersoana'])
            aIntrat=True
        else:
            #iesire 
            if(len(persoane)>0):
                idPersoana=persoane[random.randint(0,len(persoane)-1)]
                output["sens"]="out"
                output["idPersoana"]=idPersoana
                
                persoane.remove(idPersoana)
                aIntrat=True
        if(aIntrat):
            data = output
            params = {'Content-Type': 'application/json', 'Accept': '*/*'}
            json_data = json.dumps(data)
            response = requests.post(URL,data = json_data, headers= params)
            print(output)
        time.sleep(random.randint(1,5))

main()
