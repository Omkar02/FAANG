

string = 'rprprprprprprppprpprprprpr'
X = 5
Y = 7


def prStritn(string, X, Y):
    sums = 0
    string = list(string)
    cnt = 0
    while string.count('p') != 0 and string.count('r') != 0:
        print(string)
        va1, va2 = string.index('p'), string.index('r')
        print(va1, va2)

        if X > Y and va1 < va2:
            sums += X
            string[va1] = ''
            string[va2] = ''


        elif X < Y and va1 > va2:
            sums += Y
            string[va1] = ''
            string[va2] = ''

        if cnt == 100:
            break
        cnt += 1

    return sums


print(prStritn(string, X, Y))
