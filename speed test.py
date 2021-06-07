# pip install speedtest-cli lmaoo yaad rakhna zaruri hoti
from tkinter import *
from speedtest import Speedtest

def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 


root = Tk()
root.title("Internet Speed Tracker")
root.geometry('300x150')
root.resizable(0, 0)
root.wm_iconbitmap("123.ico")
button = Button(root, text="Get Speed",relief=GROOVE, width=30, command=update_text)
button.place(x=42,y=4)
down_label = Label()
down_label.place(x=60,y=50)
up_label = Label()
up_label.place(x=65,y=70)
Label(root, text="MUCk Production©",font="system 10").place(x=170,y=130)
root.mainloop()