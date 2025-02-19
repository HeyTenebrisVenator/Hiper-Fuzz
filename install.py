import os

os.system('sudo apt-get update')
os.system('sudo apt-get upgrade -y')
try:
    os.mkdir('/usr/share/hiper_fuzz')
except FileExistsError:
    print('File already exists')
os.system('sudo cp -r wordlists /usr/share/hiper_fuzz/wordlists')
os.system('sudo cp hiper_fuzz.py /usr/share/bin/hiper_fuzz')
os.system('sudo apt-get install python3-tk')
os.system('sudo apt-get install ffuf')
os.system('sudo apt install gnome-terminal')
