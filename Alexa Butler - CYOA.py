print("Welcome to Edison, you need to take have math test but in order to take the test you need to find the class")
print("find a writing utensil, and study for the math test. All in ten minutes.")
print("If you do all of this in the time frame you win the game, but if you run out of time you lose.")
print(" There are items all around the school that will help you with your game , ")
print("but be careful there are also staff members on campus ready to fight. ""Good luck!")
print("Your inventory is empty")


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
        super(Pen, self).__init__("Pen", 3, "The Pen is in the english building")

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


class Car(Item):
    def __init__(self):
        super(Car, self).__init__("Car", 12, "The car is in the parking lot")


class Helmet(Item):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", 9, "The helmet is at the school bus")


class Bandage(Item):
    def __init__(self):
        super(Bandage, self).__init__("Bandage", 4, "The bandage is in the science building ")


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
        if target.health < 0:
            target.health = 0
        print("%s deals 10 damage" % self.name)

    def interact(self, item):
        self.items += item

    def fight(self, target):
        print("You start fighting %s" % target.name)
        while self.health > 0 and target.health > 0:
            cmd = input("What do you want to do?")
            if cmd in ['attack']:
                player.attack(target)
            else:
                print("You hesitate")
            if target.health > 0:
                target.attack(player)
            if target.health <= 0:
                print("You have killed %s." % target.name)
            if self.health <= 0:
                print("You died.")
                quit(0)


player = Character("You", 100, None, None, [], "It's You")
enemy = Character("Staff", 50, None, None, [], "EVIL")
teacher = Character("Teacher", 50, None, None, [], "The teacher will give you the test")
student = Character("Student", 50, None, None, [], "I am a student")


class Room(object):
    def __init__(self, name, north, south, east, west, northeast, northwest, southwest, southeast, description,
                 items=None, characters=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northeast = northeast
        self.northwest = northwest
        self.southwest = southwest
        self.southeast = southeast
        self.description = description
        self.items = items
        self.characters = characters

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Items
key = Key()

# Initialize Rooms
amp = Room("AMP", "library", "cafe", "w_building", "english_building", "Gym", None, "science_building", None,
           "The Backpack is on the AMP", [Backpack])
library = Room("library", None, "amp", "art_building", "north_admin", None, "parking_lot", "english_building",
               "w_building", "The Book is in the Library", [Book])
cafe = Room("CAFE", "amp", "pool", "science_building", "math_building", "w_building", "english_building", "South admin",
            None, "The Flashlight is in the Cafe", [Flashlight])
Pool = Room("POOL", "cafe", None, "south_admin", None, "science_building", "math_building", None, None,
            "You are east of the south admin, there is a teacher by the pool", None, teacher)
south_admin = Room("SOUTH ADMIN", "science_building", None, "school_bus", "pool", None, "cafe", None, None,
                   "The key is in south admin", [key])
art_building = Room("ART BUILDING", None,"w_building", None, "library", None, None, "amp", None,
                    "The door is locked, The Pencil is in the Art building", [Pencil])
math_building = Room("MATH BUILDING", "english_building", None, "cafe", None, "amp", "locker_room", None, "pool",
                     "The door is locked, The test is in the math building", [Test])
w_building = Room("W BUILDING", "art_building", "science_building", None, "amp", None, "library", "cafe", None,
                  "You are west of AMP, the is a student ")
science_building = Room("SCIENCE BUILDING", "w_building", "south_admin", None, "cafe", None, "amp", "pool", "school_bus"
                        , "You are west of CAFE, there is a staff member in the science building,"
                          " there is a bandage in the building", [Bandage])
english_building = Room("ENGLISH BUILDING", "north_admin", "math_building", "amp", "gym", "parking_lot", None, "cafe",
                        None, "You are west of GYM, the pen is in the english building ", [Pen])
north_admin = Room("NORTH ADMIN", None, "english_building", "library", "parking_lot", None, None, "gym", "amp",
                   "You are west of Library, there is a computer is in the north admin", [Computer])
gym = Room("GYM", "parking_lot", "locker_room", "english_building", None, "north_admin", None, "cafe", None,
           "The Clock is in the Gym, there is a student in the gym", [Clock])
school_bus = Room("SCHOOL BUS", None, None, None, "south_admin", "science_building", None, None, None,
                  "You are west of SOUTH ADMIN, there is a helmet on the bus", [Helmet])
locker_room = Room("LOCKER ROOM", "gym", None, "math_building", None, "english_building", None, None,
                   "pool", "The Scooter is in the locker room", [Scooter])
parking_lot = Room("PARKINGLOT", None, "gym", None, "south_admin", None, None, "english_building", "gym",
                   "You are west of SOUTH ADMIN, there is a car in the parking lot", [Car])

current_node = Pool
directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southwest', 'southeast']
short_directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'sw', 'se']
use_items = ['unlock', 'pick up', 'take', 'use', 'equip', 'drop', 'look', 'turn on', 'open', 'close', 'turn off',
             'ride', 'read', 'take test', 'wear']
attack_methods = ['hit', 'punch', 'kick', 'slap', 'push']
inventory = []

while True:
    print("You are at the ", current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command tobe the long form
        command = directions[pos]

    command_found = False
    for subcommand in use_items + attack_methods:
        if subcommand in command:
            print(subcommand)
            command_found = True
            if subcommand == 'ride':
                print("You are riding the scooter")
            elif subcommand == 'unlock':
                print("You need a key if you have one open ")
            elif subcommand == 'look':
                print("You can see items")
            elif subcommand == 'drop':
                print("You dropped the item")
            elif subcommand == 'take':
                print("You took the item")
                current_node.description = "There is nothing here"
            elif subcommand == 'use':
                print("You can use the item")
            elif subcommand == 'equip':
                print("The item is equipped")
            elif subcommand == 'turn on':
                print("You turned on the item")
            elif subcommand == 'open':
                print("You opened the door")
            elif subcommand == 'close ':
                print("You closed the item")
            elif subcommand == 'turn off':
                print("You turned off the item")
            elif subcommand == 'take test':
                print("What is 5 + 5")
            elif subcommand == 'read':
                print(" 5 + 5 = 10")
            elif subcommand == 'wear':
                print("You are wearing the helmet ")
            else:
                pos = len(subcommand)
                item_name = command[pos + 1:]
                print(item_name)
            if command in ['kick', 'punch', 'push', 'slap', 'hit']:
                if current_node.characters is not None:
                    player.fight(current_node.characters)
                    current_node.description = "There is nobody here"
                    current_node.characters = None
                else:
                    print("There is nobody here")

    if command_found:
        pass
    elif command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")

    else:
        print('Command not recognized')