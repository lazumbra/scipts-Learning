from os import listdir
from os.path import isfile, join
import csv
import subprocess
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#convert only the lstQty
def convert_qty_input_to_str(line_to_convert):
    line_to_convert[9] = str(line_to_convert[9]).rjust(18, '0')
    line = line_to_convert
    line =  ','.join(line_to_convert[:])
    line_to_convert = line

def change_all_contra_broker(new_contra_broker, list_lines):
    for line in list_lines:
        line[2] = new_contra_broker.rjust(8, '0')
        #list_lines[2] = new_contra_broker
    

def group_orders_id(file_name):

    total_lines = sum(1 for line in open(file_name)) - 1

    previous_line = None
    line_to_save = None
    current_line = None
    num_in_line = 0
    final_list = []

    with open(file_name, mode='r') as csv_file:
        for i, line in enumerate(csv_file):
            file_line = line.split(',')
            file_line[-1] = file_line[-1][:-1]
            if num_in_line < 1:
                previous_line = file_line
                line_to_save = file_line
                line_to_save[9] = int(file_line[9])
            elif num_in_line >= 1 and num_in_line < total_lines:
                current_line = file_line
                if current_line[0] !=  previous_line[0]: 
                    convert_qty_input_to_str(line_to_save)
                    final_list.append(line_to_save)
                    line_to_save = current_line
                    line_to_save[9] = int(current_line[9])
                    previous_line = current_line
                else:
                    line_to_save[9] += int(current_line[9])
                    line_to_save[10] = min(line_to_save[10], current_line[10])
                    previous_line = current_line
            else:
                current_line = file_line
                if current_line[0] != previous_line[0]:
                    convert_qty_input_to_str(line_to_save)
                    final_list.append(line_to_save)
                    final_current_line =  ','.join(current_line[:])
                    convert_qty_input_to_str(current_line)
                    final_list.append(current_line)
                else:
                    line_to_save[9] += int(current_line[9])
                    line_to_save[10] = min(line_to_save[10], current_line[10])
                    line_to_save[9] = str(line_to_save[9])
                    convert_qty_input_to_str(line_to_save)
                    final_list.append(line_to_save)
            num_in_line +=1
        return final_list


def write_data_to_file(where_to_save,a_file, list_files):
    if not os.path.isdir(where_to_save + a_file[10:18]):
        os.mkdir(where_to_save + a_file[10:18])

    with open(where_to_save + a_file[10:18] + "/" + a_file, mode = 'a+') as f:
        for lines in list_files:
            line_to_save = ','.join(lines[:])
            f.write("%s\n" % line_to_save)


files_input = config['CONVORDSENDER']['input_file_data']
output_path = config['CONVORDSENDER']['output_files']
broke_number = config['CONVORDSENDER']['broker_number']

#it gets everyfile and add it into the onlyfiles list
onlyfiles = [f for f in listdir(files_input) if isfile(join(files_input, f))]
print(onlyfiles)

for a_file in onlyfiles:
    aha_to = []
    aha_to = group_orders_id( files_input + a_file )
    change_all_contra_broker(broke_number, aha_to)
    write_data_to_file(output_path, a_file, aha_to)







