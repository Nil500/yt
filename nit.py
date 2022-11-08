from os import system
from platform import machine
print('Checking For Update...')
system('git pull')
if machine()=='nit.pyc':
    system('curl -L https://github.com/Nil500/yt/blob/main/nit.pyc')
else:
    system('curl -L https://github.com/Nil500/yt/blob/main/nit.pyc')
