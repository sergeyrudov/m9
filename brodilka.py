rooms = {100:{'title':'Стартовая локация','descr':'Это страртовая локация хеви ворлд, тратата','exits':{'юг':101,'восток':102}},
              101:{'title':'Творческая мастерскя','descr':'Тут что-то происходит','exits':{'север':100,'запад':103}},
         102:{'title':'Кузница', 'descr':'Здесь куют металл','exits':{'восток':100}},
         103:{'title':'Гавань','descr':'Здесь видно корабли','exits':{'запад':101}}

         }

#старт это западно северная комнаата, восток-юг запад север
#
char = {'position':100,'inventory':[]}


def print_room(command=None):
    print(rooms[char['position']]['title'])
    print(rooms[char['position']]['descr'])


def step(command):
    if rooms[char['position']]['exits'].get(command):
        char['position'] = rooms[char['position']]['exits'][command]
        print('Вы переместились на {0}'.format(command))
        print_room()
    else:
        print('не получается попасть туда')



commands = {'смотреть': print_room, 'юг':step, 'север': step, 'восток': step, 'запад':step}

def main():
    print_room()
    print ('Доступные команды для игрока {0}'.format(','.join(list(commands.keys()))))
    while True:
        command = input()
        if commands.get(command.split()[0]):
            commands[command.split()[0]](command)
        else:
            print('такой команды не существует')
main()

