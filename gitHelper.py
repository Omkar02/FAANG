
# git add .
# git commit -m "first commit"
# git push -u origin master


import subprocess


def gitStuff(message):
    proc = subprocess.Popen(f'git statu')
    proc = subprocess.Popen(f'git add .')
    proc = subprocess.Popen(f'git commit -m "{message}"')
    proc = subprocess.Popen(f'git push -u origin master')


# print ('result: ', proc.communicate())
