world_map ={
    'AMP': {
        'NAME': "AMP",
        'DESCRIPTION': "You are west of the w building",
        'PATHS': {
            'NORTH': 'LIBRARY',
            'SOUTH': 'CAFETEIRA',
            'EAST': 'ENGLISH CLASS',
            'NORTHEAST': 'GYM',
            'SOUTHWEST': 'SCIENCE BUILDING'

        }
    },
    'LIBRARY': {
        'NAME': "L1L2",
        'DESCRIPTION': "You are west of north admin",
        'PATHS': {
            'SOUTH': 'AMP',
            'SOUTHEAST': 'W BUILDING'
        }
    },
    'CAFE': {
        'NAME': "CAFETERIA",
        'DESCRIPTION': "You are west of the science building",
        'PATHS': {
            'NORTH': 'AMP',
            'SOUTH': 'POOL'
        }
    },
    'POOL': {
        'NAME': "POOL",
        'DESCRIPTION': "You are west of the south admin",
        'PATHS': {
            'NORTH': 'CAFE',
            'EAST': 'MATH CLASS'
        }
    },
    'SOUTH ADMIN': {
        'NAME': "SOUTH ADMIN",
        'DESCRIPTION': "You are west of POOL",
        'PATHS': {
            'NORTH': 'CAFE',
            'EAST': 'MATH CLASS'
        }
    },
    'MATH CLASS': {
        'NAME': "MATH CLASS",
        'DESCRIPTION': "You are west of CAFE",
        'PATHS': {
            'NORTH': 'NORTH ADMIN',
            'SOUTH WEST': 'POOL'
        }
    },

    'GYM': {
        'NAME': "GYM",
        'DESCRIPTION': "You are west of ENGLISH CLASS",
        'PATHS': {
            'NORTHWEST': 'NORTH ADMIN',
            'SOUTH': 'LOCKER ROOM'
        }
    },

    'LOCKER ROOM': {
        'NAME': "LOCKER ROOM",
        'DESCRIPTION': "You are west of CAFE",
        'PATHS': {
            'NORTH': 'GYM',
            'SOUTHWEST': 'MATH CLASS',
            'NORTHWEST': 'GYM'
        }
    },

    'ENGLISH CLASS': {
        'NAME': "ENGLISH CLASS",
        'DESCRIPTION': "You are west of AMP",
        'PATHS': {
            'NORTH': 'NORTH ADMIN',
            'SOUTH': 'MATH CLASS',
            'EAST': 'GYM'
        }
    },
#NOT DONE ART BUILDING
   'ART BUILDING': {
        'NAME': "ART BUILDING",
        'DESCRIPTION': "You are west of LIBRARY",
        'PATHS': {
            'NORTH': 'NORTH ADMIN',
            'SOUTH': 'MATH CLASS',
            'EAST': 'GYM'
        }
    }
}


current_node =world_map['POOL']
directions = ['NORTH','SOUTH','EAST','WEST''NORTHEAST','NORTHWEST','SOUTHWEST','SOUTHEAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node =world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')
        print()


