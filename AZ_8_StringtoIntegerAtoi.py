# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def myAtoi(String):
    String = String.strip()
    if String[0] != '-' and not String[0].isnumeric():
        return 0

    ans = ''
    for i in String:
        if i == '-' or i.isnumeric():
            ans += i

    return int(ans)


String = "4193 with words"
# Output: 4193
String = "        -452"
print(myAtoi(String))
