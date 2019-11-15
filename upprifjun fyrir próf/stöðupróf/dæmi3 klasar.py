class IntList:
    def __init__(self, size):
        self.size = size
        self.my_list = []

    def __len__(self):
        return len(self.my_list)


    def add(self, i):
        if len(self.my_list) < self.size:    # ef að lengdin af listanum er minni en leyfileg stærð þá má hann halda áfram
            self.my_list.append(i)            # fyrir lista 1 bætir hann við stökum þangað til að hann kemur að cappinu hjá lista 1 sem er 5
                                            # fyrir lista 2 bætir hann við stökum að 10 því cappið á lista2 er 12 en rangeið er bara 10


    def __str__(self):
        return ("{}".format(self.my_list))

    def full(self):
        return len(self.my_list) == self.size       ## hérna checkar hann hvort að stærðin á listanum með stökunum sé sú sama og á cappinu sem var gefið

    def __add__(self, other):
        if self.size < other.size:          ## ef stærðin á cappinu á lista 1 er minni en á lista 2
            leng = self.size                ## þá er lengd = stærðin á cappinu
        else:
            leng = other.size               ## annars er lengdin = á lista 2
        new_list = IntList(leng)               ## hérna set ég nýja cappið á nýjum lista
        for i in range(leng):                   ## hérna ítra ég í gegnum listann með cappið sem er
            new_list.add(self.my_list[i] + other.my_list[i])  ## hérna plúsa ég saman það sem er er í lista 1 við lista 2 en það er cappað á 5
        return new_list



# Main program starts here
list1 = IntList(5)  # Constructs an IntList that can hold 5 integers
list2 = IntList(12) # Constructs and IntList that can hold 12 integers

for i in range(10):
    list1.add(i)
    list2.add(i)

print(list1)
print(list2)

print("Length of list1 is: {}".format(len(list1)))
print("Length of list2 is: {}".format(len(list2)))

if list1.full():
    print("list1 is full")
if list2.full():
    print("list2 is full")

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)
