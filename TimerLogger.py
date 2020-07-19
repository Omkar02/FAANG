# import subprocess
import datetime
import os
from gitHelper import gitStuff


gitStuff(message='Inillized Time logger')

# cwd = ['C:/Users/omkar/Desktop/Python_Projects/CodeingProblems/Stuff', 'C:/Users/omkar/Desktop/Python_Projects/CodeingProblems/']


def CodeTimeLogging(Flag, filename):
    prevEntry = getPreviousEntryDict()

    if filename not in prevEntry:
        if Flag == 'S':
            prevEntry[filename] = {'StartDate': datetime.datetime.now().date(),
                                   'EndDate': None,
                                   'StartTime': datetime.datetime.now().strftime('%I:%M:%S %p'),
                                   'EndTime': None,
                                   'Duration': None}
            # subprocess.call('git add . ', shell=True)
            # subprocess.call(f'git commit -m "Inillized {filename}"', cwd=cwd[0], shell=True)
            # subprocess.call(f'git commit -m "Inillized {filename}"', cwd=cwd[1], shell=True)
        else:
            raise Exception('Wrong Flag for the File!')

    elif filename in prevEntry and Flag == 'F' and prevEntry[filename]['EndTime'] == 'None':
        prevEntry[filename]['EndDate'] = datetime.datetime.now().date()
        prevEntry[filename]['EndTime'] = datetime.datetime.now().strftime('%I:%M:%S %p')

        prevStartTime = prevEntry[filename]['StartDate'] + '|' + prevEntry[filename]['StartTime']
        StartTimeDuration = datetime.datetime.strptime(prevStartTime, '%Y-%m-%d|%I:%M:%S %p')

        duration_in_s = (datetime.datetime.now() - StartTimeDuration).total_seconds()
        prevEntry[filename]['Duration'] = int(divmod(duration_in_s, 60)[0])

        # subprocess.call(f'git commit -m "Finished{filename}"', cwd=cwd[0], shell=True)
        # subprocess.call(f'git commit -m "Finished{filename}"', cwd=cwd[1], shell=True)

    # subprocess.call('git push -f origin master', shell=True)
    saveEntry(prevEntry)


def saveEntry(taskInfo):
    os.remove('loggingInfo.csv')

    with open('loggingInfo.csv', 'w') as w:
        w.write('Name, StartDate, EndDate, StartTime, EndTime, Duration\n')

    for keys, val in taskInfo.items():

        StartDate = val['StartDate']
        EndDate = val['EndDate']
        StartTime = val['StartTime']
        EndTime = val['EndTime']
        Duration = val['Duration']

        with open('loggingInfo.csv', 'a') as a:
            a.write(f'{keys}, {StartDate}, {EndDate}, {StartTime}, {EndTime}, {Duration}\n')


def getPreviousEntryDict():
    entryDict = {}
    with open('loggingInfo.csv') as r:
        information = r.read().split('\n')[1:-1]

    for allInfo in information:
        Name, StartDate, EndDate, StartTime, EndTime, Duration = allInfo.split(',')

        entryDict[Name] = {'StartDate': None,
                           'EndDate': None,
                           'StartTime': None,
                           'EndTime': None,
                           'Duration': None}

        currDict = entryDict[Name]

        currDict['StartDate'] = StartDate.strip()
        currDict['EndDate'] = EndDate.strip()
        currDict['StartTime'] = StartTime.strip()
        currDict['EndTime'] = EndTime.strip()
        currDict['Duration'] = Duration.strip()

    return entryDict


# if os.path.exists("Stuff") == False:
#     os.makedirs('Stuff')

if not os.path.exists('loggingInfo.csv'):
    with open('loggingInfo.csv', 'w') as w:
        pass


import __main__ as main

fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='S', filename=fileName)
