from tkinter import *
import requests
import os
window = Tk()
window.title("Hiper Fuzz")
wordlist = ''
wl = ''
cookie = StringVar(window)
url_var = StringVar(window)
header_txt = StringVar(window)
rate_txt = StringVar(window)
output_txt = StringVar(window)
status = ''

wordlist_local = '/usr/share/hiper_fuzz/'

def SetURL():
    url = url_var.get()
    lbl2['text'] = f'Checking connection with {url}'
    try:
        status = requests.get(url).status_code
        lbl2['text'] = f'Connection done, receive status code {status}'
        return 'OK'
    except:
        lbl2['text'] = 'Error connecting to the URL'
        return 'ERROR'






def Start():
    extra_data = ''
    if cookie.get() != '':
        extra_data += f'-H "Cookie: {cookie.get()}"'
    if rate_txt.get() != '':
        extra_data += f' -rate {rate_txt.get()}'
    if header_txt.get() != '':
        extra_data += f' -H "{header_txt.get()}"'
    if output_txt.get() != '':
        extra_data += f' -o "{output_txt.get()}"'
    if SetURL() == 'OK' and lbl4['text'] != '':
        os.system(f'sudo gnome-terminal -- sh -c  \'ffuf {extra_data} -s -sf -recursion -w {wordlist_local}/{lbl4['text'].replace('Wordlist: ', '')} -u {url_var.get()}/FUZZ; bash\'')
    else:
        lbl5['text'] = 'Please, complete the configuration'

window.geometry('1200x900')
window.tk.call('tk', 'scaling', '3.0')

title = Label(window, text='HIPER FUZZ')
title.config(font=("Courier-Bold", 30))
title.grid(column=0, row=0)

lbl2 = Label(window, text='Insert the URL here >>')
lbl2.grid(column=0, row=1)

url = Entry(window, textvariable=url_var)
url.grid(column=1, row=1)

enter = Button(window, text='Enter', command=SetURL)
enter.grid(column=2, row=1)

lbl2 = Label(window, text='Waiting for URL...')
lbl2.grid(column=4, row=1)

lb3 = Label(window, text='SELECT A WORDLIST')
lb3.grid(column=1, row=2)

lbl4 = Label(window, text='')
lbl4.grid(column=6, row=0)

start = Button(window, text='Start Fuzzing', command=Start)
start.grid(column=5, row=0)

lbl5 = Label(window, text='')
lbl5.grid(column=0, row=3)

lbl6 = Label(window, text='EXTRA')
lbl6.grid(column=1, row=19)




cookies = Entry(window, textvariable=cookie)
cookies.grid(column=1, row=20)

lbl6 = Label(window, text='Cookies')
lbl6.grid(column=0, row=20)




header = Entry(window, textvariable=header_txt)
header.grid(column=1, row=21)

lbl7 = Label(window, text='Header (txt:txt)')
lbl7.grid(column=0, row=21)





rate = Entry(window, textvariable=rate_txt)
rate.grid(column=1, row=22)

lbl7 = Label(window, text='Rate Limit(req/seconds)')
lbl7.grid(column=0, row=22)

out = Entry(window, textvariable=output_txt)
out.grid(column=1, row=23)

lbl7 = Label(window, text='Save Output')
lbl7.grid(column=0, row=23)
#wordlist1
def Wordlist1():
    wordlist = 'wordlists/common.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist1 = Button(window, text='common list', command=Wordlist1)
wordlist1.grid(column=1, row=3)




#wordlist2
def Wordlist2():
    wordlist = 'wordlists/big.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist2 = Button(window, text='big list', command=Wordlist2)
wordlist2.grid(column=1, row=4)




#wordlist3
def Wordlist3():
    wordlist = 'wordlists/apache.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist3 = Button(window, text='Apache', command=Wordlist3)
wordlist3.grid(column=1, row=5)




#wordlist4 
def Wordlist4():
    wordlist = 'wordlists/cvePaths.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Common CVEs', command=Wordlist4)
wordlist4.grid(column=1, row=6)

def Wordlist5():
    wordlist = 'wordlists/iis.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='IIS', command=Wordlist5)
wordlist4.grid(column=1, row=7)

def Wordlist6():
    wordlist = 'wordlists/tomcat.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Tomcat', command=Wordlist6)
wordlist4.grid(column=1, row=8)
def Wordlist7():
    wordlist = 'wordlists/oracle.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Oracle', command=Wordlist7)
wordlist4.grid(column=1, row=9)

def Wordlist8():
    wordlist = 'wordlists/frontpage.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='frontpage', command=Wordlist8)
wordlist4.grid(column=1, row=10)
def Wordlist9():
    wordlist = 'wordlists/aspx.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='ASPX', command=Wordlist9)
wordlist4.grid(column=1, row=11)

def Wordlist10():
    wordlist = 'wordlists/graphql.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Graphql', command=Wordlist10)
wordlist4.grid(column=1, row=12)

def Wordlist11():
    wordlist = 'wordlists/weblogic.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Web Logic', command=Wordlist11)
wordlist4.grid(column=1, row=13)

def Wordlist12():
    wordlist = 'wordlists/logins.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Logins Fuzz', command=Wordlist12)
wordlist4.grid(column=1, row=14)

def Wordlist13():
    wordlist = 'wordlists/api_common.txt'
    lbl4['text'] = f'Wordlist: {wordlist}'
wordlist4 = Button(window, text='Common API endpoints', command=Wordlist13)
wordlist4.grid(column=1, row=15)
window.mainloop()