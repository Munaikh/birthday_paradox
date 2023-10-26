# A function that converts a day number to DD/MM format
import datetime

test = {'Lisa': 26, 'Christopher': 28, 'Richard': 247, 'Paul': 66,
        'Sandra': 41, 'Barbara': 337,
        'Christopher-6': 227, 'Dorothy': 70, 'Sandra-8': 2, 'Lisa-9': 81,
        'Joseph': 87, 'Richard-11': 324, 'John': 122,
        'Linda': 158, 'Patricia': 52, 'Martha': 95, 'Donald': 135,
        'Karen': 114, 'Karen-18': 361, 'Nancy': 235, 'Nancy-20': 250,
        'Jessica': 35, 'Paul-22': 318}


def convert_day(day_num):
    day_obj = datetime.date.fromordinal(day_num)
    dd_mm_str = day_obj.strftime("%d/%m")
    # Print the dd/mm string
    return dd_mm_str


def change_dict(dict: list):
    for i in range(len(dict)):
        for key, value in dict[i].items():
            dict[i][key] = convert_day(value)
    return dict
