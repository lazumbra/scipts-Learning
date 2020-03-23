import json

if __name__ == '__main__':
    print('a casa caiu')

    file_to_read = '/home/jefferson/Downloads/296e1724-1232-4e50-a963-3edd851e9be1.csv'
    print('oi')
    with open(file_to_read, 'r') as fp:
        for line in fp.readlines():
            line = line.split(' ')

            print(len(line))