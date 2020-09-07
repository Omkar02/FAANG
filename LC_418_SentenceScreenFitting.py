# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Medium')


"""
public int wordsTyping(String[] sentence, int rows, int cols) {
        String str = "";
         
        for (String word : sentence) {
            str += word + " ";
        }
         
        int len = str.length();
         
        int start = 0;
        for (int i = 0; i < rows; i++) {
            start += cols;
             
            if (str.charAt(start % len) == ' ') {
                start++;
                continue;
            }
             
            while ((start % len - 1 >= 0) && str.charAt(start % len - 1) != ' ') {
                start--;
            }
        }
         
        return start / len;
    }
}
"""


def wordsTyping(rows, cols, sentence):
    string = ''
    for word in sentence:
        string += word + ' '

    n = len(string)
    start = 0
    for i in range(rows):
        start += cols
        if string[start % n] == ' ':
            start += 1
            continue

        while start % n - 1 >= 0 and string[start % n - 1] != " ":
            start -= 1

    return int(start / n)


def wordsTyping(rows, cols, sentence):
    total = rows * cols
    string = ' '.join(sentence) + ' '

    return int(total / len(string))


rows = 2
cols = 8
sentence = ["hello", "world"]

rows = 3
cols = 6
sentence = ["a", "bcd", "e"]

rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]

print(wordsTyping(rows, cols, sentence))
