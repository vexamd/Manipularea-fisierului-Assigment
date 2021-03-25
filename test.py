def sub(a, b):
    return a-b
with open ('./expression.txt', 'r') as f:
    with open ('./output.txt', 'w') as g:
        lines = f.readlines()
        for l in lines:
            if  '-' in l:
                 operands = l.split('-')
                 rez = sub(int(operands[0]), int(operands[1]))
                 g.write(operands[0] + "-" + operands[1].rstrip() + "=" + str(rez) + "\n")