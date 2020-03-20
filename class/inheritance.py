class Phone:
    def __init__(self):
        print("I'm in phone class")

    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class Samsung(Phone):
    def __init__(self):
       super().__init__()
       print("I'm in samsung class")

    def message(self):
        print("You can send message")

    def photo(self):
        print("You can take photos")


s = Samsung()
s.call()
s.message()
s.photo()


