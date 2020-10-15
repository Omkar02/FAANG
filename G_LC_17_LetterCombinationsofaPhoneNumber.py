# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def letterCombinations(digits):
    output = []
    keypad = {'1': " ", '2': "abc", '3': "def",
              '4': "ghi", '5': "jkl", '6': "mno",
              '7': "pqrs", '8': "tuv", '9': "wxyz", '0': " "}
    backtrack("", digits, 0, keypad, output)
    return output


def backtrack(combination, digits, idx, keypad, output):
    if idx == len(digits):
        output.append(combination)

    else:
        for letter in keypad[digits[idx]]:
            backtrack(combination + letter, digits, idx + 1, keypad, output)


digits = "23"
print(letterCombinations(digits))

print([1, 2, 3, 4][1:])
