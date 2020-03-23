import os.path
import csv

if __name__ == '__main__':
    file_to_read = '/home/jefferson/Documents/test_files/13-02-2020/resultado_csv/final_result.csv'
    
    path_to_save = 'final_result_modified.csv'

    fileEmpty = os.stat(path_to_save).st_size == 0

    with open(file_to_read, 'r') as fp:
        for line in fp.readlines():
            line_to_save = None
            list_line = line.split(',')
            month = list_line[0][4:6]
            day = list_line[0][6:8]
            symbol = list_line[1][:4]
            print('line: ',list_line, len(list_line))

            if symbol[:3] == 'WDO':
                if month == '12' and day < '31' and symbol == 'WDOF':
                    #print('WDOF')
                    line_to_save = line 
                elif month == '01' and day < '30' and symbol == 'WDOG':
                    #print('WDOG')
                    line_to_save = line
            else:
                if month == '12' and day < '18' and symbol == 'WINZ':
                    #print('WINZ')
                    line_to_save = line
                elif (month == '12' and day > '17' and symbol == 'WING') or (month == '01' and day < '30' and symbol == 'WING'):
                    #print('arquivo para copiar')
                    line_to_save = line
            
            with open(path_to_save, mode='a') as csv_file:
                fieldnames = ['Date', 'Symbol', 'Max Pos', 'Clip', 'Rebalance', 'Position', 'Buy Orders', 'Sell Orders'
                , 'Buy Contracts', 'Sell Contracts', 'Efficiency', 'Efficacy', 'Profit', 'MTM Profit']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if line_to_save != None:
                    print(line_to_save)
                    csv_file.write(line_to_save)
            

