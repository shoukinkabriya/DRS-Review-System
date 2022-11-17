import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag
    
def pending(decision):
    #1 display decision_panding_image
    frame=cv2.cvtColor(cv2.imread('decision_panding_image.jpg'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #2 wait for 1 second
    time.sleep(1)
    #3 display sponser_image
    frame=cv2.cvtColor(cv2.imread('sponser.jpg'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #4 wait for 1.5 second
    time.sleep(1.5)
    #5 display out/not out image
    if decision == 'Out':
        decisionImg = 'Out.jpg'
    else :
        decisionImg = 'notout.jpg'
    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
     

    pass

def out():
    thread=threading.Thread(target=pending,args=('Out',))
    thread.daemon=1
    thread.start()
    print('player is out')
def not_out():
    thread=threading.Thread(target=pending,args=('Not out',))
    thread.daemon=1
    thread.start()
    print('player is not out')

SET_WIDTH=650
SET_HEIGHT=368
window=tkinter.Tk()
window.title("Shoukin Third Umpire Decison ")
cv_image=cv2.cvtColor(cv2.imread('Fg3zgyhUUAAh9sd.jpg'),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


# buttons to control play back
btn=tkinter.Button(window,text="<<Previous (fast)",width=50,command=partial(play,-25))
btn.pack()
btn=tkinter.Button(window,text="<<Previous (slow)",width=50,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="Next (slow) >>",width=50,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window,text="Next (fast) >>",width=50,command=partial(play,25))
btn.pack()
btn=tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn=tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()



window.mainloop()