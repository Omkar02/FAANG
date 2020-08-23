

string = 'rprprprprprprppprpprprprpr'
X = 5
Y = 7


def prStritn(string, X, Y):
    sums = 0
    string = list(string)
    while string.count('p') != 0 and string.count('r') != 0:
        print(string)
        va1, va2 = string.index('p'), string.index('r')

        if X > Y and va1 < va2:
            sums += X
            string[va1] = ''
            string[va2] = ''

        else:
            sums += Y
            string[va1] = ''
            string[va2] = ''
    return sums


print(prStritn(string, X, Y))
