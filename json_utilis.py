import json

FILE="data/stud.json"

def read_json():
    with open(FILE) as f:
        data=json.load(f)
        return data
    
def write_json(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=3)
        