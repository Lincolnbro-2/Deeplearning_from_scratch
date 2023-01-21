import simple_gate

def XOR(x1, x2):
    s1 = simple_gate.NAND(x1, x2)
    s2 = simple_gate.OR(x1, x2)
    y = simple_gate.AND(s1,s2)
    return y

if __name__ == '__main__':
    for x in [(0,0), (1,0), (0,1), (1,1)]:
        y = XOR(x[0], x[1])
        print(str(x) + " -> " + str(y))