from json_utilis import *


def registration(name,age,address,course):
    data=read_json()
    temp_data={"sno":len(data["student"])+1,
        "name":name,
               "age":age,
               "address":address,
               "course":course
    }
    data["student"].append(temp_data)
    write_json(data)
def updatestud(id,name,address,age,course):
    data=read_json()
    for student in data["student"]:
        if str(student["sno"])==id:
            student["name"]=name
            student["address"]=address
            student["age"]=age
            student["course"]=course
            break
    write_json(data)


def deletestud(id):
    data=read_json()
    for student in data["student"]:
        if str(student["sno"])==id:
            data["student"].remove(student)
            break

    i=1
    for student in data["student"]:
        student["sno"]=i
        i+=1
    write_json(data)