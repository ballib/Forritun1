class House:
    def __init__(self, door=0, window=0):
        self.door = door
        self.window = window

    def set_door(self, otherdoor):
        self.door = otherdoor

    def get_door(self):
        return self.door

    def __str__(self):
        return f'Þetta hus er með {self.door} hurðum og {self.window} gluggum'


h1 = House(777, 9999) # Nýtt hús
print(h1.door) # None
h1.set_door(5)

print(h1.get_door()) # 5

h2 = House(20, 1000) # Annað nýtt hús

print(h1.door)  # 5
print(h2.door)  # 20

print(h1)  # Þetta hus er með 5 hurðum og 9 gluggum