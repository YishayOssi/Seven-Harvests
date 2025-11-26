class Soldier:
    def __init__(self, id:int, first_name:str, last_name:str, gender:str, city:str, Distance_from_base:int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.Distance_from_base = Distance_from_base
        self.Placement_status = False

    def __dict__(self):
      return {"id":self.id, "first_name":self.first_name, "last_name":self.last_name, "gender":self.gender, "city":self.city, "Distance_from_base":self.Distance_from_base}

class Room(Soldier):
    def __init__(self):
       self.room = []

  


class Building(Room):
    def __init__(self):
        self.list_of_room = []



class Seven_Harvests:
    def __init__(self):
      self.List_of_Building = []
      self.List_of_soldiers = []



base = Seven_Harvests()

b1 = Building()
name_of_room1 = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8"]
for i in name_of_room1:
   i = Room()
   b1.list_of_room.append(i)

b2 = Building()
name_of_room2 = ["r9", "r10", "r11", "r12", "r13", "r14", "r15", "r16"]
for j in name_of_room2:
   j = Room()
   b2.list_of_room.append(j)


s1 = Soldier(2, "yishay", "ossi", "z", "netanta", 35)
    





        

    