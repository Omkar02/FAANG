# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='String', Difficult='Hard')


class English:
    def __init__(self):
        self.under20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                        "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.places = ["Hundred", "Thousand", "Million", "Billion"]

    def numbetToWords(self, num):
        return ('Zero' if num == 0 else ' '.join(filter(None, self.help(num))))

    def help(self, num):
        if num < 20:
            return [self.under20[num]]

        elif num < 100:
            return [self.tens[num // 10]] + self.help(num % 10)

        elif num < 1000:
            return self.help(num // 100) + [self.places[0]] + self.help(num % 100)

        elif num < 1000000:
            return self.help(num // 100) + [self.places[1]] + self.help(num % 1000)

        elif num < 1000000000:  # millions
            return self.help(num // 1000000) + [self.places[2]] + self.help(num % 1000000)

        else:  # billions
            return self.help(num // 1000000000) + [self.places[3]] + self.help(num % 1000000000)


num = 121
e = English()

print(e.numbetToWords(num))
