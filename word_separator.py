

fileName = '/home/jefferson/Downloads/Logs_24_27(2)/FIX.4.4-IORA5001-DCE305.messages.log.20200127T143405.339074'

with open(fileName, 'r') as fp:
    for line in fp.readlines():
        print('who is my line', line)

        if '|' in line:
            print('tem um pipe na string')
            exit()
        if '\x01' in line:
            print('ele tem o outro caracter. Pode sair do for')
            exit()
