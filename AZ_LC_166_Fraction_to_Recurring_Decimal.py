# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def fractionToDecimal(numerator, denominator):
    sign = '-' if (numerator * denominator) < 0 else ''
    integer, remainder = divmod(numerator, denominator)
    seen = {}
    decimal = ''
    while remainder > 0:
        last_remainder = remainder
        digi, remainder = divmod(remainder * 10, denominator)
        seen[last_remainder] = len(decimal)
        decimal += str(digi)
        if remainder in seen:
            index = seen[remainder]
            decimal = f'{decimal[:index]}({decimal[index:]})'
            break
    ans = sign + str(integer)
    if decimal:
        ans += f'.{decimal}'
    return ans


numerator = 22
denominator = 7
print(fractionToDecimal(numerator, denominator))
