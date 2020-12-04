# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


# R(right), L(left), U(up), and D(down).


def robotToOrigin(moves):
    x = y = 0
    for action in moves:
        if action == 'U':
            y -= 1
        elif action == 'D':
            y += 1
        elif action == 'L':
            x -= 1
        else:
            x += 1
        print(x, y)

    return (x, y) == (0, 0)


moves = "U"
print(robotToOrigin(moves))
