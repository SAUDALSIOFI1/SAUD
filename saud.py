'''name=input('enter your name:')
print('welcome Mr',name)

want=input('what you want do?')
print('okay just wait')'''

'''
while True:
    try:
        num=int(input('please enter your number:'))    
        la=int(input('please enter your password:'))
except:
     print('please enter number !!')

-------------------------------------------------------------------------------
import os
files =os.listdir ('pictures')
for file in files :
    print(files)
    ---------------------------------------------------------------------------'''

'''try :
    conn=mysql.connector.connect(
        host ='localhost ',
        user='root',
        passw=''

    )
    mycur=conn.cursor()
    mycur.execute("CREATE DATABASE SAUD")
except mysql.connector.Eroor as r :
    print(r)'''

'''while True :
    exam= int (input('enter the answer: 10 + 30 :'))
    if (exam) == 40 :
        print('wow very good student ')
        break
    else :
        print('false ,try again ')
------------------------------------------------------
import socket 
hname = input('enter the url:')
ip =socket.gethostbyname(hname)
print(ip) 
#-------------------------------------------------------

import socket 
hostname ='www.google.com'
hn= socket.getfqdn(hostname)
print(hn)
-------------------------------------------------------
                  اله حاسبه
 int(input('enter first number'))
op=input('enter operator')#+ - * /
num2= int(input('enter second number'))
if op == '+' :
    print(num1+num2)
if op == '-':
    print(num1-num2)
if op =='*':
    print(num1*num2)
if op =='/':
    print(num1/num2)
-------------------------------------------------------
import emoji 
print(emoji.emojize('hiiiiiiii saud :red_heart:'))
------------------------------------------------------------
                 AGE 
import datetime 
now= datetime.datetime.now()
age=int(input('enter your birthday:'))
year=now.year
rx=(year-age)
print('your age is :',rx)
----------------------------------------------------------

import webbrowser
webbrowser.open ('www.google.com')
,

if you want to search in your browser 
import webbrowser
webbrowser.open('enter your bowser/search?=your search') 
-----------------------------------------------------------
import pyautogui 
import time 
while True:
    time.sleep(2)
    pyautogui.typewrite('if you want send message in your time \n')
    time.sleep(6)
    pyautogui.typewrite('if you want send message in yourB time')
--------------------------------------------------------------------

name = input ('enter your name:')
print ('hi  welcome :',name )'''
from turtle import *
forward(40)
right (40)