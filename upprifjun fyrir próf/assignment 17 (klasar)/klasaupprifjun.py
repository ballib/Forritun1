class Counter:
    def __init__(self, value=0):
        self.value = value  # self.value is an instance variable, tilvikabreyta


    def __str__(self):
        return "Counter value: {}".format(self.value)
    def increment(self, value=1):
        self.value += value

    def decrement(self, value =1):
        self.value -= value

# interface for class is the set of methods that it defines

# Main program starts here
counter1 = Counter()    # calling the constructor (smiður)
counter1.increment()    # counter1 is self in the call to increment
counter1.increment(3)   # increment counter by value
counter1.decrement(1)   # decrement counter by value
print(counter1)
