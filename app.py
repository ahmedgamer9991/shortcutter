from tkinter import *
from tkinter import ttk
import webbrowser as wb
import os

import prg

# Functions


def youtube(event=None):
    wb.open('www.youtube.com')


def google(event=None):
    wb.open('www.google.com')


def tiktok(event=None):
    wb.open('www.tiktok.com')


def speedtyping(event=None):
    wb.open('https://www.speedtypingonline.com/typing-tutor.php?mod=8')


def wit_anime(event=None):
    wb.open('https://witanime.com/')


def shut_down(event=None):
    os.system("shutdown -p")


def terminal(event=None):
    os.system("cd .. && start powershell")


# def games(event=None):
#     os.system(r"start C:\Users\ahmed\Desktop\games")


def restartFunc(event=None):
    os.system(r"shutdown /r /t 0")


def sleepFunc(event=None):
    os.system(r"rundll32 powrprof.dll,SetSuspendState 0,1,0")


width = 300
height = 370
w = Tk()
w.title("by ahmedkhoukh")
x, y = int((w.winfo_screenwidth())/2) - \
    int(width/2), int((w.winfo_screenheight())/2)-int(height/2)-20
w.geometry(f"{width}x{height}+{x}+{y}")

##########    Photos    ##########
gogle = PhotoImage(file=r'imgs\google.png')
youtbe = PhotoImage(file=r'imgs\youtu4be.png')
tiktik = PhotoImage(file=r'imgs\tiktok.png')
speedtypin = PhotoImage(
    file=r'imgs\STO_logo_wText.png')
witanime = PhotoImage(file=r'imgs\\WITLOGO.png')
shutdown = PhotoImage(
    file=r'imgs\toggl_app_64px.png')
terminall = PhotoImage(
    file=r'imgs\console_64px.png')
# gamess = PhotoImage(
#     file=r'imgs\games_folder_64px.png')
etc = PhotoImage(
    file=r'imgs\Plus Math.png')
restart = PhotoImage(
    file=r'imgs\Restart.png')
sleep = PhotoImage(
    file=r'imgs\Sleep.png')
icon = PhotoImage(
    file=r'imgs\icons8_python_64px_3.png')
w.iconphoto(True, icon)
###################################

# buttons
youtubebtn = ttk.Button(
    w,
    command=youtube,
    # font=('arial',20),
    image=youtbe
)
googlebtn = ttk.Button(
    w,
    command=google,
    # font=('arial',20),
    image=gogle
)
tiktokbtn = ttk.Button(
    w,
    command=tiktok,
    # font=('arial',20),
    image=tiktik
)
witanimebtn = ttk.Button(
    w,
    command=wit_anime,
    # font=('arial',20),
    image=witanime
)
speedbtn = ttk.Button(
    w,
    command=speedtyping,
    # font=('arial',20),
    image=speedtypin
)
shutbtn = ttk.Button(
    w,
    command=shut_down,
    # font=('arial',10),
    image=shutdown
)
terminalbtn = ttk.Button(
    w,
    command=terminal,
    image=terminall
)
# gamesbtn = ttk.Button(
#     w,
#     command=games,
#     image=gamess
# )
prgbtn = ttk.Button(
    w,
    command=prg.new.test2,
    image=etc
)
restartbtn = ttk.Button(
    w,
    command=restartFunc,
    image=restart
)
sleepbtn = ttk.Button(
    w,
    command=sleepFunc,
    image=sleep
)

# binds
w.bind('<Key-1>', youtube)
w.bind('<Key-2>', google)
w.bind('<Key-3>', tiktok)
w.bind('<Key-4>', wit_anime)
w.bind('<Key-5>', speedtyping)
w.bind('<Key-6>', shut_down)
w.bind('<Key-7>', restartFunc)
w.bind('<Key-8>', sleepFunc)

youtubebtn.pack(ipady=7, pady=[22, 8], expand=True)
googlebtn.pack(ipady=2, pady=8, expand=True)
tiktokbtn.pack(ipady=2, pady=8, ipadx=2, expand=True)
witanimebtn.pack(ipady=2, pady=8, expand=True)
speedbtn.pack(ipady=2, pady=8, expand=True)
shutbtn.place(x=15, y=15, width=43, height=43)
terminalbtn.place(x=242, y=15, width=43, height=43)
# gamesbtn.place(x=242, y=15, width=43, height=43)
prgbtn.place(x=242, y=70, width=43, height=43)
restartbtn.place(x=15, y=70, width=43, height=43)
sleepbtn.place(x=15, y=125, width=43, height=43)

w.mainloop()
