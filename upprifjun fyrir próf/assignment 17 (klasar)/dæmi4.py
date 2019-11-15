class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def str_update(self, clock=""):
        clock = clock.split(":")
        self.hours = clock[0]
        self.minutes = clock[1]
        self.seconds = clock[2]

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes and {self.seconds} seconds"

    def add_clocks(self):



clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
#clock3 = clock1.add_clocks(clock2)
#print(clock3)