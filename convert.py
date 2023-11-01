# A function that converts a day number to DD/MM format
import datetime


# This function takes a day number as input and returns a string in DD/MM format
def convert_day(day_num):
    day_obj = datetime.date.fromordinal(day_num)
    dd_mm_str = day_obj.strftime("%d/%m")
    return dd_mm_str


# This function takes a list of dictionaries as input and returns a list of dictionaries with the day numbers converted
def change_dict(dict: list):
    for i in range(len(dict)):
        for key, value in dict[i].items():
            dict[i][key] = convert_day(value)
    return dict
