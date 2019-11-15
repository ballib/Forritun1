class Sentence:
    def __init__(self, setn):
        self.setn = setn.split()

    def get_first_word(self):
        return self.setn[0]

    def get_all_words(self):
        return self.setn

    def replace(self, index, new_word):
        self.setn[index] = new_word











sent = Sentence("This is a test")
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())