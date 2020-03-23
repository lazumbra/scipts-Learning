import json

if __name__ == '__main__':

    file_to_read = '/home/jefferson/Documents/test_files/13-02-2020/output_file/20200123/DF_WING20_20200123.csv'

    with open(file_to_read, 'r') as fp:
        for line in fp.readlines():
            info = map(str, line.split(','))
            info = list(info)
            price =  float(info[12])  
            if price <= 0:
                print('incorrect price')
            #info = json.loads(line)
