import tkinter
import webapp
import session
import os
from threading import Thread

there_is_session = False
path = ""

def center_window(root,w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def threaded_function2():
    global there_is_session
    while(not there_is_session):
        global there_is_session
    global path
    sessions = session.IdSession(path)
    r = sessions.getAccountInformation()
    print(type(sessions.getStatusCode(r)))
    if(sessions.getStatusCode(r) == 200):
        window = tkinter.Tk()
        window.title("Success")
        center_window(window,200,200)
        label = tkinter.Label(window, text = "You Profile has been loaded").pack()
        label = tkinter.Label(window, text = "Close This window!").pack()
        window.mainloop()
    else:
        window = tkinter.Tk()
        window.title("Failed")
        center_window(window,200,200)
        label = tkinter.Label(window, text = "An Error Occurred").pack()
        label = tkinter.Label(window, text = "loading your profile").pack()
        label = tkinter.Label(window, text = "Close This Window!").pack()
        window.mainloop()
    
def btn5u(s1,s2):
    f = open("client_inf.txt","w")
    f.write(s1+"\n")
    f.write(s2)
    f.close()

def bt2(s):
    try:
        f = open("../bin/"+s+".bin", 'rb')
        f.close()
        global path
        path = "../bin/"+s+".bin"
        global there_is_session
        there_is_session = True
    except :
        window = tkinter.Tk()
        center_window(window,200,200)
        window.geometry("200x200")
        label = tkinter.Label(window, text = "This profile has not been saved").pack()
        label = tkinter.Label(window, text = "try to create a session!").pack()
       
if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("OpenSource Lichess Bot")
    center_window(window,390,380)
    window.resizable(0, 0)
    
    #top_frame = tkinter.Frame(window).pack()
    #bottom_frame = tkinter.Frame(window).pack(side = "bottom")
    tkinter.Label(window, text = "Client Id").grid(row = 0) # this is placed in 0 0
    # 'Entry' is used to display the input-field
    entry1 = tkinter.Entry(window) # this is placed in 0 1
    entry1.grid(row = 0, column = 1) # this is placed in 0 1

    tkinter.Label(window, text = "Client Secret").grid(row = 1) # this is placed in 1 0
    entry2 = tkinter.Entry(window) # this is placed in 1 1
    entry2.grid(row = 1, column = 1) # this is placed in 1 1
    tkinter.Label(window, text = "Lichess profile").grid(row = 22,column = 1) # this is placed in 1 0
    entry3 = tkinter.Entry(window) # this is placed in 1 1
    entry3.grid(row = 25, column = 1) # this is placed in 1 1
    
    # now, create some widgets in the top_frame and bottom_frame
    btn0 = tkinter.Button(window, text = "Create Web Application", fg = "black", height = 5, width = 20)
    btn1 = tkinter.Button(window, text = "Create Session", fg = "red", height = 5, width = 20)
    btn2 = tkinter.Button(window, text = "Load Lichess Profile", fg = "green", command=lambda :  bt2(entry3.get()))
    btn3 = tkinter.Button(window, text = "Select Lichess Board", fg = "purple").grid(row = 40, column = 1)
    btn4 = tkinter.Button(window, text = "Let The bot Play", fg = "orange").grid(row = 50, column = 1)
    btn5 = tkinter.Button(window, text = "Save Client Inf", fg = "yellow", command=lambda :  btn5u(entry1.get(),entry2.get()))

    btn0.bind("<Button-1>", webapp.bt0)
    btn0.grid(row = 2, column = 1)
    btn1.bind("<Button-1>", webapp.bt1)
    btn1.grid(row = 20, column = 1)
    btn5.grid(row = 0, column = 2)
    btn2.grid(row = 30, column = 1)
    
    thread = Thread(target = threaded_function2)
    thread.start()
    
    window.mainloop()
    thread.join()
    
    
    

