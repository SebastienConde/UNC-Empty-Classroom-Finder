from collections import defaultdict
from bisect import insort
import re


def hall_refactor(hall):
    buildings = {'Global Center': 'FedEx Global Education Center',
                 'Administrative Offic': 'Administrative Office Bldg',
                 'Brauer Hall': 'Brauer Hall',
                 'Koury Oral Health Sc': 'Koury Oral Health Sciences Bldg',
                 'Wilson Library': 'Wilson Library',
                 'Abernethy Hall': 'Abernathy Hall',
                 'Rams Head Recreation': 'Rams Head Recreation Center',
                 'Loudermilk Hall': 'Loudermilk Hall',
                 'Genetic Medicine Res': 'Genetic Medicine Research Bldg',
                 'Love House': 'Love House',
                 'Naval Armory': 'Naval Armory',
                 'Mary Ellen Jones': 'Mary Ellen Jones Bldg',
                 'McColl Bldg': 'McColl Bldg',
                 'Howell Hall': 'Howell Hall',
                 'Swain Hall': 'Swain Hall',
                 'Phillips Hall': 'Phillips Hall',
                 'Graham Student Union': 'Graham Student Union',
                 'Bioinformatics Bldg': 'Bioinformatics Bldg',
                 'Communication Media ': 'Communication Media',
                 'Bondurant Hall': 'Bondurant Hall',
                 'Campus Y': 'Campus Y',
                 'Smith Middle School ': 'Smith Middle School',
                 'Hooker Research Cent': 'Hooker Research Center',
                 'Medical Biomolecular': 'Medical Biomolecular Research Bldg',
                 'Graham Memorial': 'Graham Memorial Hall',
                 'Fetzer Hall': 'Fetzer Hall',
                 'Person Hall': 'Person Hall',
                 'Van Hecke-Wettach Ha': 'Van Hecke-Wettach Hall',
                 'MacNider Hall': 'MacNider Hall',
                 'Global Education, Fe': 'FedEx Global Education Center',
                 'Kerr Hall': 'Kerr Hall',
                 'Kenan Labs': 'Kenan Labs',
                 'Kenan Center': 'Kenan Center',
                 'New East': 'New East',
                 'McGavran-Greenberg H': 'McGavran-Greenberg Hall',
                 'Art Studio Bldg': 'Art Studio Bldg',
                 'Gardner Hall': 'Gardner Hall',
                 'Murray Hall': 'Murray Hall',
                 'Hanes Hall': 'Hanes Hall',
                 'Coker Hall': 'Coker Hall',
                 'Curtis Media Center': 'Curtis Media Center',
                 'ITS Manning': 'ITS Manning',
                 'Genome Sciences Buil': 'Genome Sciences Bldg',
                 'Koury Res Hall': 'Koury Residence Hall',
                 'Carolina Hall': 'Carolina Hall',
                 'Craige North Res Hal': 'Craige North Residence Hall',
                 'Manning Hall': 'Manning Hall',
                 'Hamilton Hall': 'Hamilton Hall',
                 'Health Sciences Libr': 'Health Sciences Library',
                 'Greenlaw Hall': 'Greenlaw Hall',
                 'Mitchell Hall': 'Mitchell Hall',
                 'Tate-Turner-Kuralt B': 'Tate-Turner-Kuralt Bldg',
                 'Rosenau Hall': 'Rosenau Hall',
                 'Kenan Music Bldg': 'Kenan Music Bldg',
                 'Davie Hall': 'Davie Hall',
                 'Paul Green Theater ': 'Paul Green Theater ',  # Why extra space here?
                 'Marsico Hall': 'Marsico Hall',
                 'Murphey Hall': 'Murphey Hall',
                 'Woollen Gym': 'Woollen Gym',
                 'Smith Bldg': 'Smith Bldg',
                 'Gillings Dramatic Ar': 'Center for Dramatic Art',
                 'Karpen Hall': 'Karpen Hall',
                 'Hill Hall': 'Hill Hall',
                 'Dey Hall': 'Dey Hall',
                 'Carroll Hall': 'Carroll Hall',
                 'Cobb Res Hall': 'Cobb Residence Hall',
                 'New West': 'New West',
                 'Sitterson Hall (incl': 'Sitterson Hall',
                 'Stone Center': 'Stone Center',
                 'Alumni Bldg': 'Alumni Bldg',
                 'Chapman Hall': 'Chapman Hall',
                 'Knapp-Sanders Bldg ': 'Knapp-Sanders Bldg',
                 'Morehead Chemistry L': 'Morehead Chemistry Labs',
                 'Peabody Hall': 'Peabody Hall',
                 'Venable Hall': 'Venable Hall',
                 'Wilson Hall': 'Wilson Hall',
                 'Caldwell Hall': 'Caldwell Hall',
                 'Hanes Art Center': 'Hanes Art Center',
                 'Beard Hall': 'Beard Hall'}
    if hall in buildings.keys():
        return buildings[hall].lower().strip()
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
        return ('ITS Manning')
    elif building == 'mcgavran-greenberg hall':
        return ('McGavran-Greenberg Hall')
    elif building == 'mccoll bldg':
        return ('McColl Bldg')
    elif building == 'fedex global education center':
        return ('FedEx Global Education Center')
    elif building == 'macnider hall':
        return ('Macnider Hall')
    else:
        return (f'{building.title()}')
