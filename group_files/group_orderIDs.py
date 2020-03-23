from os import listdir
from os.path import isfile, join
import csv
import subprocess
import os


#convert only the lstQty
def convert_qty_input_to_str(line_to_convert):
    line_to_convert[9] = str(line_to_convert[9]).rjust(18, '0')
    line = line_to_convert
    line =  ','.join(line_to_convert[:])
    line_to_convert = line

my_path = '/home/jefferson/Downloads/format_order_sender/'
output_path = '/home/jefferson/Downloads/files_grouped/'



def change_all_contra_broker(new_contra_broker, list_lines):
    for line in list_lines:
        line[2] = new_contra_broker.rjust(8, '0')
        #list_lines[2] = new_contra_broker
    

def group_orders_id(file_name):

    total_lines = sum(1 for line in open(file_name)) - 1
    print("Total de linhas menos 1 =",total_lines)


    previous_line = None
    line_to_save = None
    current_line = None
    num_in_line = 0
    final_list = []

    with open(file_name, mode='r') as csv_file:
        for i, line in enumerate(csv_file):
            file_line = line.split(',')
            file_line[-1] = file_line[-1][:-1]
            #print("Acredito que aqui ele vai imprimir linha", num_in_line)
            if num_in_line < 1:
                previous_line = file_line
                line_to_save = file_line
                line_to_save[9] = int(file_line[9])
                print(num_in_line)
                #print("previous_line: ", previous_line)
            elif num_in_line >= 1 and num_in_line < total_lines:
                current_line = file_line
                print(num_in_line)
                if current_line[0] !=  previous_line[0]: #Eu so salvo quando as linhas forem diferentes
                    #salvar line to save IMPORTANTE
                    #print("salvar linha: ", line_to_save)
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
                print("Quem e o tamanho: ",num_in_line)
                current_line = file_line
                if current_line[0] != previous_line[0]:
                    #salvar buffer
                    #converter para str novamentte
                    #line_to_save[9] = str(line_to_save[9])
                    #final_line_to_save =  ','.join(line_to_save[:])
                    #convert_qty_input_to_str(line_to_save)
                    #print("salvar penultima: ", line_to_save)
                    convert_qty_input_to_str(line_to_save)
                    final_list.append(line_to_save)
                    #salvar line_to_save
                    final_current_line =  ','.join(current_line[:])
                    #print("salvar ultima: ", current_line)
                    convert_qty_input_to_str(current_line)
                    final_list.append(current_line)
                    
                    print('Cheguei na utima linha e sao diferentes')
                else:
                    line_to_save[9] += int(current_line[9])
                    line_to_save[10] = min(line_to_save[10], current_line[10])
                    #salvar a line_to_save
                    #converter para str novamentte
                    line_to_save[9] = str(line_to_save[9])
                    #print("salvar linha: ", line_to_save)
                    convert_qty_input_to_str(line_to_save)
                    final_list.append(line_to_save)
                    print("Cheguei na ultima linha e são iguais")
            #print(file_line[-1][:-2], file_line[9], file_line[10])
            #file_line[-1] = file_line[-1][:-2]
            #d1 =  ','.join(file_line[:])
            #print(d1)
            num_in_line +=1
        return final_list


def write_data_to_file(where_to_save,a_file, list_files):
    #DF_WDOG20_20200117.csv
    #/home/jefferson/Documents/20200113/DF_WDOG20_20200113.csv
    #file_name_is = 'DF_' + list_files[7] + '_' + origin_files[4:12] + '.csv'
    if not os.path.isdir(where_to_save + a_file[10:18]):
        os.mkdir(where_to_save + a_file[10:18])

    with open(where_to_save + a_file[10:18] + "/" + a_file, mode = 'w') as f:
        for lines in list_files:
            line_to_save = ','.join(lines[:])
            f.write("%s\n" % line_to_save)



#it gets everyfile and add it into the onlyfiles list
onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]
print(onlyfiles)


for a_file in onlyfiles:
    aha_to = []
    aha_to = group_orders_id('/home/jefferson/Downloads/format_order_sender/'+ a_file)
    change_all_contra_broker('90', aha_to)
    write_data_to_file("/home/jefferson/Downloads/bora_ver/", a_file, aha_to)


'''
aha_to = []
aha_to = group_orders_id('/home/jefferson/Downloads/vai_dar_certo/WDO_20191202.txt')
for linha in aha_to:
    print(linha)

print("nao muda",onlyfiles[0][4:12])

os.system('cd /home/jefferson/Downloads/vai_dar_certo/')
print(os.system('pwd'))
'''

#min:  DF_WINZ19_20191211.csv
for min_lin in onlyfiles:
    print("min: ", min_lin[10:18])


#print("aha_to", len(aha_to))


#for linha in aha_to:
#    print(linha)



#print("aha[0]", ','.join(aha_to[0][:]))



