from cProfile import label
from logging import exception


currentAddr = 0

labels = []

def assemble(mode, file):
    asm = open(file)
    output = ""
    global currentAddr
    global labels
    while True:
        line = asm.readline()
        if not line:
            break

        line = line.replace(',', '')
        line = line.replace('\n', '')
        line = line.split(' ')

        if mode == 0:
            if line[0] == '$':
                labels.append(line[1])
                conv = hex(currentAddr)[2:]

                strPad = ''
                for i in range(0, 4 - len(conv)):
                    strPad += '0'

                labels.append(strPad + conv)



        if line[0] == 'nop':
            output += '00 '
            currentAddr += 1


        if line[0] == 'jmp':

            if line[1] == '$':
                if mode == 1:
                    addr = labels.index(line[2]) + 1

                output += '06 '
                currentAddr += 1
                currentAddr += 1
                currentAddr += 1

                if mode == 1:
                    output += (labels[addr][2] + labels[addr][3] + ' ')
                    output += (labels[addr][1] + labels[addr][0] + ' ')

            else:
                output += '06 '
                currentAddr += 1
                output += line[2]
                output += ' '
                currentAddr += 1
                output += line[1]
                output += ' '
                currentAddr += 1


        if line[0] == 'add':
            if line[1] == 'a':
                if line[2] == 'b':
                    output += '05 '
                    currentAddr += 1
                    output += '01 '
                    currentAddr += 1


        if line[0] == 'out':
            if line[2] == 'a':
                output += '07 '
                currentAddr += 1
                output += (line[1] + ' ')
                currentAddr += 1
            if line [2] == 'b':
                output += '08 '
                currentAddr += 1
                output += (line[1] + ' ')
                currentAddr += 1
            if line [2] == 'c':
                output += '09 '
                currentAddr += 1
                output += (line[1] + ' ')
                currentAddr += 1
            if line [2] == 'd':
                output += '0a '
                currentAddr += 1
                output += (line[1] + ' ')
                currentAddr += 1
                


        if line[0] == 'mov':
            if '(' in line[2]:

                if line[1] == 'a':
                    output += '20 '

            if line[1] == 'a':
                if line[2] == 'a':
                    continue
                if line[2] == 'b':
                    output += '0e '
                    currentAddr += 1
                    continue
                if line[2] == 'c':
                    output += '0f '
                    currentAddr += 1
                    continue
                if line[2] == 'd':
                    output += '10 '
                    currentAddr += 1
                    continue
            if line[1] == 'b':
                if line[2] == 'a':
                    output += '0b '
                    currentAddr += 1
                    continue
                if line[2] == 'b':
                    continue
                if line[2] == 'c':
                    output += '11 '
                    currentAddr += 1
                    continue
                if line[2] == 'd':
                    output += '12 '
                    currentAddr += 1
                    continue
            if line[1] == 'c':
                if line[2] == 'a':
                    output += '0c '
                    currentAddr += 1
                    continue
                if line[2] == 'b':
                    output += '13 '
                    currentAddr += 1
                    continue
                if line[2] == 'c':
                    continue
                if line[2] == 'd':
                    output += '14 '
                    currentAddr += 1
                    continue
            if line[1] == 'd':
                if line[2] == 'a':
                    output += '0d '
                    currentAddr += 1
                    continue
                if line[2] == 'b':
                    output += '15 '
                    currentAddr += 1
                    continue
                if line[2] == 'c':
                    output += '16 '
                    currentAddr += 1
                    continue
                if line[2] == 'd':
                    continue


            
            if line[1] == 'a':
                output += '01 '
                currentAddr += 1
            if line[1] == 'b':
                output += '02 '
                currentAddr += 1
            if line[1] == 'c':
                output += '03 '
                currentAddr += 1
            if line[1] == 'd':
                output += '04 '
                currentAddr += 1

            output += line[2]
            output += ' '
            currentAddr += 1
    
    return output
        
        
print(assemble(0, "test.lgasm"))
print(currentAddr)

print(labels)

print(assemble(1, "test.lgasm"))