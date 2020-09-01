# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def isPossible(nums):
    digits = {x: nums.count(x) for x in set(nums)}
    theTemp = set(nums)
    W = 3
    while digits:
        currNum = min(theTemp)
        for i in range(currNum, currNum + W):
            if i not in digits:
                return False

            if digits[i] == 1:
                del digits[i]
                theTemp.remove(i)

            else:
                digits[i] -= 1

    return True


nums = [1, 2, 3, 3, 4, 5]
nums = [1, 2, 3, 3, 4, 4, 5, 5]

print(isPossible(nums))
