from collections import defaultdict
from bisect import insort
import re

def hall_refactor(hall):
    buildings = {'Global Center', 'Administrative Offic', 'Brauer Hall', 'Koury Oral Health Sc', 'Wilson Library', 'Abernethy Hall', 'Rams Head Recreation', 'Loudermilk Hall', 'Genetic Medicine Res', 'Love House', 'Naval Armory', 'Mary Ellen Jones', 'McColl Bldg', 'Howell Hall', 'Swain Hall', 'Phillips Hall', 'Graham Student Union', 'Bioinformatics Bldg', 'Communication Media ', 'Bondurant Hall', 'Campus Y', 'Smith Middle School ', 'Hooker Research Cent', 'Medical Biomolecular', 'Graham Memorial', 'Fetzer Hall', 'Person Hall', 'Van Hecke-Wettach Ha', 'MacNider Hall', 'Global Education, Fe', 'Kerr Hall', 'Kenan Labs', 'Kenan Center', 'New East', 'McGavran-Greenberg H', 'Art Studio Bldg', 'Gardner Hall', 'Murray Hall', 'Hanes Hall', 'Coker Hall', 'Curtis Media Center', 'ITS Manning', 'Genome Sciences Buil', 'Koury Res Hall', 'Carolina Hall', 'Craige North Res Hal', 'Manning Hall', 'Hamilton Hall', 'Health Sciences Libr', 'Greenlaw Hall', 'Mitchell Hall', 'Tate-Turner-Kuralt B', 'Rosenau Hall', 'Kenan Music Bldg', 'Davie Hall', 'Paul Green Theater ', 'Marsico Hall', 'Murphey Hall', 'Woollen Gym', 'Smith Bldg', 'Gillings Dramatic Ar', 'Karpen Hall', 'Hill Hall', 'Dey Hall', 'Carroll Hall', 'Cobb Res Hall', 'New West', 'Sitterson Hall (incl', 'Stone Center', 'Alumni Bldg', 'Chapman Hall', 'Knapp-Sanders Bldg ', 'Morehead Chemistry L', 'Peabody Hall', 'Venable Hall', 'Wilson Hall', 'Caldwell Hall', 'Hanes Art Center', 'Beard Hall'}
    if hall in buildings:
        if hall == 'Mary Ellen Jones':
            return 'Mary Ellen Jones Bldg'
        elif hall == 'Hooker Research Cent':
            return 'Hooker Research Center'
        elif hall == 'Medical Biomolecular':
            return 'Medical Biomolecular Research Bldg'
        elif hall == 'Graham Memorial':
            return 'Graham Memorial Hall'
        elif hall == 'Van Hecke-Wettach Ha':
            return 'Van Hecke-Wettach Hall'
        elif hall == 'Global Education, Fe':
            return 'FedEx Global Education Center'
        elif hall == 'McGavran-Greenberg H':
            return 'McGavran-Greenberg Hall'
        elif hall == 'Genome Sciences Buil':
            return 'Genome Sciences Bldg'
        elif hall == 'Koury Res Hall':
            return 'Koury Residence Hall'
        elif hall == 'Craige North Res Hal':
            return 'Craige North Residence Hall'
        elif hall == 'Health Sciences Libr':
            return 'Health Sciences Library'
        elif hall == 'Tate-Turner-Kuralt B':
            return 'Tate-Turner-Kuralt Bldg'
        elif hall == 'Gillings Dramatic Ar':
            return 'Center for Dramatic Art'
        elif hall == 'Cobb Res Hall':
            return 'Cobb Residence Hall'
        elif hall == 'Sitterson Hall (incl':
            return 'Sitterson Hall'
        elif hall == 'Morehead Chemistry L':
            return 'Morehead Chemistry Labs'
        elif hall == 'Genetic Medicine Res':
            return 'Genetic Medicine Research Bldg'
        elif hall == 'Rams Head Recreation':
            return 'Rams Head Recreation Center'
        elif hall == 'Koury Oral Health Sc':
            return 'Koury Oral Health Sciences Bldg'
        elif hall == 'Administrative Offic':
            return 'Administrative Office Bldg'
        elif hall == 'Global Center':
            return 'FedEx Global Education Center'
        else:
            return hall.lower().strip()
    raise Exception('Building not in building set')

def time_refactor(time):
    time = time.replace(':', '')
    time = time.replace(' - ', '')
    return time


def day_refactor(list_of_classes):
    day_to_time_dict = defaultdict(list)
    for college_class in list_of_classes:
        day = college_class.days
        if 'm' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['monday']:
                insort(day_to_time_dict['monday'], time_refactor(college_class.time))
        if 'tu' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['tuesday']:
                insort(day_to_time_dict['tuesday'], time_refactor(college_class.time))
        if 'w' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['wednesday']:
                insort(day_to_time_dict['wednesday'], time_refactor(college_class.time))
        if 'th' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['thursday']:
                insort(day_to_time_dict['thursday'], time_refactor(college_class.time))
        if 'f' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['friday']:
                insort(day_to_time_dict['friday'], time_refactor(college_class.time))
        if 'sa' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['saturday']:
                insort(day_to_time_dict['saturday'], time_refactor(college_class.time))
        if 'su' in day:
            if time_refactor(college_class.time) not in day_to_time_dict['sunday']:
                insort(day_to_time_dict['sunday'], time_refactor(college_class.time))
    return day_to_time_dict


def military_to_standard(time):
    reg_match = [r'13:', r'14:', r'15:', r'16:', r'17:', r'18:', r'19:', r'20:', r'21:', r'22:', r'23:', r'24:']
    reg_repl = ['01:', '02:', '03:', '04:', '05:', '06:', '07:', '08:', '09:', '10:', '11:', '12:']
    for i in range(len(reg_match)):
        time = re.sub(reg_match[i], reg_repl[i], time)
    return time

def title_refactor(building):
    if building == 'its manning':
        return('ITS Manning')
    elif building == 'mcgavran-greenberg hall':
        return('McGavran-Greenberg Hall')
    elif building == 'mccoll bldg':
        return('McColl Bldg')
    elif building == 'fedex global education center':
        return('FedEx Global Education Center')
    elif building == 'macnider hall':
        return('Macnider Hall')
    else:
        return(f'{building.title()}')