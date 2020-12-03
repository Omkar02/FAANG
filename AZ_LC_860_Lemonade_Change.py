# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def lemonade(money):
    five = ten = 0
    n = len(money)
    for price in money:
        if price == 5:
            five += 1
        elif price == 10:
            if not five:
                return
            five -= 1
            ten += 1
        else:
            if five and ten:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


money = [5, 5, 5, 10, 20]
print(lemonade(money))
