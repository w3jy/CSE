class Item(object):

    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description


class Computer(Item):

    def __init__(self):
        super(Computer, self).__init__("Computer", 10, "The computer is in the Library")


class Pen(Item):
    def __init__(self):
        super(Pen, self).__init__("Pen", 3, "The Pen is in the Pool")

    def write(self):
        print("2")


class Test(Item):
    def __init__(self):
        super(Test, self).__init__("Test", 5, "The test is in the math building")


class Key (Item):
    def __init__(self):
        super(Key, self).__init__("Key", 7, "The key is in south admin")

    def use(self):
        pass


class Backpack (Item):
    def __init__(self):
        super(Backpack, self).__init__("Backpack", 8, "The Backpack is on the AMP")

    def use(self):
        print("Put in Backpack")


class Book (Item):

    def __init__(self):
        super(Book, self).__init__("Book", 9, "The Book is in the Library")


def use(self):
        print("5 + 5 =10")


class Clock (Item):
    time = 30

    def __init__(self):
        super(Clock, self).__init__("Clock", 6, "The Clock is in the Gym")

    def use(self):
        print("30 minutes left")


class Flashlight(Item):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight", 8, "The Flashlight is in the Cafe")

    def use(self):

        print("The Flashlight is on")


class Scooter (Item):
    def __init__(self):
        super(Scooter, self).__init__("Scooter", 12, "The Scooter is in the locker room")

    def use(self):
        self.running = True

    def drive_forward(self):
        if self.running:
            print("You move forward.")
        else:
            print("Nothing Happens.")


class Pencil(Item):
    def __init__(self):
        super(Pencil, self).__init__("Pencil", 3, "The Pencil is in the Art building")

    def write(self):
        print("5")


class Character(object):
    def __init__(self, name, health, dialogue, status, inventory, description):
        self.name = name
        self.health = health
        self.dialogue = dialogue
        self.status = status
        self.inventory = []
        self.description = description
        self.items = []

    def attack(self, target):
        target.health -= 10
        print("%s deals 10 damage" % self.name)

    def interact(self, item):
        self.items += item
