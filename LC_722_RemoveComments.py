# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def removeComments(source):
    in_block = False
    ans = []
    for line in source:
        i = 0
        if not in_block:
            newline = []
        while i < len(line):
            if line[i:i + 2] == '/*' and not in_block:
                in_block = True
                i += 1
            elif line[i:i + 2] == '*/' and in_block:
                in_block = False
                i += 1
            elif not in_block and line[i:i + 2] == '//':
                break
            elif not in_block:
                print(line[i])
                newline.append(line[i])
            i += 1
        if newline and not in_block:
            ans.append("".join(newline))

    return ans


source = ["/*Test program */",
          "int main()", "{ ",
          "  // variable declaration ",
          "int a, b, c;",
          "/* This is a test",
          "   multiline  ", "   comment for ",
          "   testing */",
          "a = b + c;", "}"]


# print(removeComments(source))
