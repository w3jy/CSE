class Room(object):
    def __init__(self, name,  north, south, east, west, northeast, northwest,southwest, southeast, description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
AMP = Room("AMP", "Library", "Cafe", "WBuilding", "Englishbuilding", "Gym", None, "Sciencebuilding", None,"You are east of the w building")

LIBRARY = Room("LIBRARY", None, "AMP", "ARTbuilding", "NORTHADMIN", None, "PARKINGLOT", "ENGLISHBUILDING", "WBUILDING", "You are east of north admin")

CAFE = Room("CAFE", "AMP", "POOL", "SCIENCEBUILDING", "Mathbuilding", "W building", "Englishbuilding",  "Adminsouth", None, "You are east of the science building")

POOL = Room("POOL", "CAFE", None, "SOUTHADMIN", None, "SCIENCEBUILDING", "MATHBUILDING", None, None, "You are east of the south admin")

SOUTHADMIN = Room("SOUTHADMIN", "SCIENCEBUILDING", None, "SCHOOLBUS", "POOL", None, "CAFE", None, None, "You are west of POOL")

ARTBUILDING = Room("ARTBUILDING", None,"WBUILDING", None, "LIBRARY", None, None, "AMP", None, "You are west of LIBRARY")

MATHBUILDING = Room("MATHBUILDING", "ENGLISHBUILDING", None, "CAFE", None, "AMP", "LOCKERROOM", None, "POOL", "You are east of CAFE")

WBUILDING = Room("WBUILDING", "ARTBUILDING", "SCIENCEBUILDING", None, "AMP", None, "LIBRARY", "CAFE", None, "You are west of AMP")

SCIENCEBUILDING = Room("SCIENCEBUILDING", "WBUILDING", "SOUTHADMIN", None, "CAFE", None, "AMP", "POOL", "SCHOOLBUS", "You are west of CAFE")

ENGLISHBUILDING = Room("ENGLISHBUILDING", "NORTHADMIN", "MATHBUILDING", "AMP", "GYM", "PARKINGLOT", None, "CAFE", None, "You are west of GYM")

NORTHADMIN = Room("NORTHADMIN", None, "ENGLISHBUILDING", "LIBRARY", "PARKINGLOT", None, None, "GYM", "AMP", "You are west of Library")

GYM = Room("GYM", "PARKINGLOT", "LOCKERROOM", "ENGLISHBUILDING", None, "NORTHADMIN", None, "CAFE", None, "You are east of ENGLISHBUILDING")

SCHOOLBUS = Room("SCHOOLBUS", None, None, None, "SOUTHADMIN", "SCIENCEBUILDING", None, None, None, "You are west of SOUTHADMIN")

LOCKERROOM = Room("LOCKERROOM", "GYM", None, "MATHBUILDING", None, "ENGLISHBUILDING", None, None, "POOL", "You are east of MATHBUILDING")

PARKINGLOT = Room("PARKINGLOT", None, "GYM", None, "SOUTHADMIN", None, None, "ENGLISHBUILDING", "GYM", "You are west of SOUTHADMIN")

current_node = POOL
directions = ['north', 'south','east', 'west', 'northeast', 'northwest', 'southwest', 'southeast']
short_directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'sw', 'se']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command tobe the long form
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')
        print()
