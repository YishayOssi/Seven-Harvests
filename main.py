from fastapi import FastAPI
import uvicorn 
from classes import *
import csv


#בניית בסיס
base = Seven_Harvests()
#בניית בנין א
b1 = Building()
#בניית 8 חדרים והכנסה לבניין
name_of_room1 = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8"]
for i in name_of_room1:
   i = Room()
   b1.list_of_room.append(i)
#בניית בנין ב
b2 = Building()
#בניית 8 חדרים והכנסה לבניין
name_of_room2 = ["r9", "r10", "r11", "r12", "r13", "r14", "r15", "r16"]
for j in name_of_room2:
   j = Room()
   b2.list_of_room.append(j)
#הכנסת 2 הבניינים לבסיס
base.List_of_Building.append(b1)
base.List_of_Building.append(b2)

s1 = Soldier(2, "yishay", "ossi", "z", "netanta", 35)




app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}



@app.get("/search")
def aaa():
   return {s1.city}



