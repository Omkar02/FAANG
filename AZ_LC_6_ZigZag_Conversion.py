# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def sConvert(s, numRows):
    if numRows == 1:
        return s
    lines = [''] * numRows
    line_count = 0
    adder = 1
    for char in s:
        lines[line_count] += char
        if line_count + adder > numRows - 1:
            adder = -1
        elif line_count + adder < 0:
            adder = 1
        line_count += adder
    return ''.join(lines)


s = "PAYPALISHIRING"
numRows = 3

print(sConvert(s, numRows))
# "PAHNAPLSIIGYIR"
