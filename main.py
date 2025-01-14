from pdf_scraper import building_set, room_set, class_dict, pdf_scraper
from refactoring_funcs import day_refactor, military_to_standard, title_refactor
from os import system

if __name__ == '__main__':
    print("Enter the corresponding letter for the year's semester section book would you like to search.")
    print('A: 2024 Spring Semester')
    print('B: 2024 Summer Semester')
    print('C: 2024 Fall Semester')
    ssb_input = input().lower().strip()
    while ssb_input not in {'a', 'b', 'c'}:
        print('Invalid input. Please enter A, B, or C.".')
        ssb_input = input().lower().strip()


    pdf_scraper(ssb_input)
    cont = True
    while cont:
        print('Please enter a building. If you would like a list of buildings to choose from, enter "Building List" (without quotes):')
        building_input = input().lower().strip()
        while building_input == 'building list' or building_input not in building_set:
            if building_input == 'building list':
                print('You may choose from one of the following buildings:')
                for building in building_set:
                    print(f'    {title_refactor(building)}')
                print('Please enter one of these buildings. If you would like to see the list again, re-enter "Building List":')
                building_input = input().lower().strip()
            elif building_input not in building_set:
                print('Sorry, that building is not listed in the Semester Section Book. Please check to make sure you have correctly entered the building name, or try a different building.')
                building_input = input().lower().strip()

        print('Please enter a room number within that building. If you would like a list of rooms in the building you selected, enter "Room List" (without quotes):')
        room_input = input().lower().strip()
        while room_input == 'room list' or room_input not in room_set[building_input]:
            if room_input == 'room list':
                print('You may choose from one of the following rooms:')
                for room in dict.fromkeys(room_set[building_input]):
                    print(f'    {room}'.title())
                print('Please enter one of these rooms. If you would like the list again, re-enter "Room List":')
                room_input = input().lower().strip()
            elif room_input not in room_set[room_input]:
                print('Sorry, that room is either not listed in the Semester Section Book, or is not located in the building you have selected. Please check to make sure you have correctly entered the room number, or try a different room. To see a list of all available rooms, enter "Room List" (without quotes):')
                room_input = input().lower().strip()
        print(f'You have selected {title_refactor(building_input)} room {room_input.title()}. This room is occupied at the following times. Please note that the room may also be occupied at times not listed below.')
        input_key = f'{building_input} : {room_input}'
        list_of_classes = class_dict[input_key]
        day_dict = day_refactor(list_of_classes)

        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            if day in day_dict.keys():
                print('--------------------', day.title(), sep='\n')
                for time in day_dict[day]:
                    print(military_to_standard(f'{time[0:2]}:{time[2:4]} - {time[4:6]}:{time[6:8]}'))
                print('--------------------', '\n')
        print('Would you like to search for another building? Enter "yes" or "no":')
        cont_input = input().lower().strip()
        while cont_input not in ['yes', 'no']:
            print('Please enter "yes" or "no":')
            cont_input = input().lower().strip()
        if cont_input == 'no':
            cont = False