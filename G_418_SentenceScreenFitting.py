# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


def wordsTyping(sentence, rows, cols):
    sentence = " ".join(sentence) + " "
    n = len(sentence)
    total = 0
    for i in range(rows):
        total += cols
        if sentence[total % n] == ' ':
            total += 1
        else:
            while total > 0 and sentence[(total - 1) % n] != ' ':
                total -= 1

    return int(total / n)


rows = 3
cols = 6
sentence = ["a", "bcd", "e"]
print(wordsTyping(sentence, rows, cols))
