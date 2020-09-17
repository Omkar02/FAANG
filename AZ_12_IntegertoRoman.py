# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def intToRoman(num):
    # units
    cur_dict = {9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI', 5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I', 0: ''}
    roman = cur_dict[num % 10]
    num = num // 10

    # tens
    cur_dict = {9: 'XC', 8: 'LXXX', 7: 'LXX', 6: 'LX', 5: 'L', 4: 'XL', 3: 'XXX', 2: 'XX', 1: 'X', 0: ''}
    roman = cur_dict[num % 10] + roman
    num = num // 10

    # hundreds
    cur_dict = {9: 'CM', 8: 'DCCC', 7: 'DCC', 6: 'DC', 5: 'D', 4: 'CD', 3: 'CCC', 2: 'CC', 1: 'C', 0: ''}
    roman = cur_dict[num % 10] + roman
    num = num // 10

    # thousands
    cur_dict = {3: 'MMM', 2: 'MM', 1: 'M', 0: ''}
    roman = cur_dict[num % 10] + roman

    return roman


print(intToRoman(123))


def romanToInt(s):
    # only consider neighboring digits, when previous digit is larger than current digit, add previous number to result; else substract previous number from result
    digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    currSum = digits[s[len(s) - 1]]
    for i in range(len(s) - 1, 0, -1):
        cur = digits[s[i]]
        pre = digits[s[i - 1]]
        currSum += pre if pre >= cur else -pre
    return currSum


print(romanToInt(intToRoman(123)))
