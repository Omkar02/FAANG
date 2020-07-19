
# git add .
# git commit -m "first commit"
# git push -u origin master


import subprocess


def gitStuff(message):
    proc = subprocess.Popen(f'git status')
    proc = subprocess.Popen(f'git add -A')
    proc = subprocess.Popen(f'git status')

    # proc = subprocess.Popen(f'git commit -m "{message}"')
    # proc = subprocess.Popen(f'git push -u origin master')


# print ('result: ', proc.communicate())
