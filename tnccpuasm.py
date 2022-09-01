asm = open('test.lgasm')
while True:
    line = asm.readline()
    if not line:
        break

    line = line.replace(',', '')
    line = line.replace('\n', '')
    line = line.split(' ')

    if line[0] == 'add':
        