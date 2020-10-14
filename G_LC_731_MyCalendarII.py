# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


class MyCalendar:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                print("false")
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        print("true")
        return True


m = MyCalendar()
m.book(10, 20)  # returns true
m.book(50, 60)  # returns true
m.book(10, 40)  # returns true
m.book(5, 15)  # returns false
m.book(5, 10)  # returns true
m.book(25, 55)  # returns true
