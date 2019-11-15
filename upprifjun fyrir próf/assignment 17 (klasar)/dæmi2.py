class RockGuitar:

    def __init__(self, guitarist="", guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar

    def set_entry(self, guitarist, guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar



    def __str__(self):
        return ("{:<20s}{:<20s}".format(self.guitarist, self.guitar))




g1 = RockGuitar()
g1.set_entry("Jimmy page", "Gibson Les Paul Standard")
g2 = RockGuitar()
g2.set_entry("Angus Young","Jaydee SG")
g3 = RockGuitar("Mark knoppfler")
print(g1)
print(g2)
print(g3)