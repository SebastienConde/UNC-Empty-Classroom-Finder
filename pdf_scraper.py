import pymupdf
import re
from collections import defaultdict
from tqdm import tqdm
from college_class import CollegeClass
from refactoring_funcs import hall_refactor

doc = r'pdf_file_goes_here'

bldg_pattern = r'(?s)Bldg: (.*?)(?=Room|\n)'  # matches 'Bldg: "
room_pattern = r'(?s)Room: (.*?)(?=Days|\n)'  # matches 'Room: '"
days_pattern = r'(?s)Days: (.*?)(?=Time|\n)'  # matches 'Days: '"
time_pattern = r'(?s)(?<!Run )Time: (.*?)(?=INST|\n)'  # matches 'Time: ' but excludes 'Run Time: '"

building_set = set()   # set to hold all building names for future searching
room_set = defaultdict(list)   # set to hold all room names indexed by buildings
class_dict = defaultdict(list)  # dict where keys are building and room, and values are days and class times


def pdf_scraper():
    pdf = pymupdf.open(doc)

    for i in tqdm(range(pdf.page_count), desc='Generating classroom hash table', unit='pages'):
        text = pdf[i].get_text()  # text on current page of pdf

        bldg_matches = re.findall(bldg_pattern, text)  # list of regex matches for bldg
        room_matches = re.findall(room_pattern, text)  # list of regex matches for room
        day_matches = re.findall(days_pattern, text)  # list of regex matches for days
        time_matches = re.findall(time_pattern, text)  # list of regex matches for times

        for i in range(len(bldg_matches)):
            if bldg_matches[i] != 'TBA' and room_matches[i] != 'TBA' and day_matches[i] != 'TBA' and time_matches[i] != 'TBA':
                current_class = CollegeClass(hall_refactor(bldg_matches[i]).lower().strip(), room_matches[i].lower().strip(), day_matches[i].lower().strip(), time_matches[i].lower().strip())

                building_set.add(current_class.building.lower().strip())  # adds current building to set
                room_set[current_class.building].append(current_class.room.lower().strip())   # adds room to set keyed by building

                dict_key = f'{current_class.building} : {current_class.room}'
                class_dict[dict_key].append(current_class)


