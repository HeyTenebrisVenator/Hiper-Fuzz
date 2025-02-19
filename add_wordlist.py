import os

local = input('Path to the wordlist  >>  ')
try:
    open(local)
except:
    print('Could not open')
    exit()
name = input('Name of the wordlist  >>  ')

try:
    os.listdir('/usr/share/hiper_fuzz')
    os.listdir('/usr/share/hiper_fuzz/wordlists')
except:
    print('ERROR: Could not find /usr/share/hiper_fuzz/wordlists. Consider running install.py to create the directory correctly')
    exit()

os.system(f'sudo cp -r {local} /usr/share/hiper_fuzz/wordlists')
print(f'Wordlist {local} added successfully')
print(f'Analyzing hiper_fuzz.py')
hiper_fuzz = open('hiper_fuzz.py', 'r').read()
value = 1

while True:
    if f'def Wordlist{value}' in hiper_fuzz:
        value += 1
        pass
    else:
        break


new_wordlist_command = f"""
def Wordlist{value}():
    wordlist = 'wordlists/{local.split('/')[-1].replace(' ', '')}'
    lbl4['text'] = f'Wordlist: {{wordlist}}'
wordlist4 = Button(window, text='{name}', command=Wordlist{value})
wordlist4.grid(column=1, row={value + 2})
window.mainloop()"""

print(new_wordlist_command)

print('Command created')
print('Regenerating hiper_fuzz.py')

final_script = ""
hiper_fuzz = open('hiper_fuzz.py', 'r').readlines()
for line in hiper_fuzz:
    line = line.replace('\n', '')
    if 'window.mainloop()' in line:
        line = line.replace('window.mainloop()', new_wordlist_command)
    final_script += line + '\n'

print('Script generated successfully')
print('Recreating hiper_fuzz.py')


print(final_script)

try:
    open('hiper_fuzz.py', 'w').write(final_script)
    print('DONE')
except:
    print('Could not write to hiper_fuzz.py')
    exit()

os.system('sudo python3 install.py')
