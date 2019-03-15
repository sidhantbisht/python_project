from tkinter import *
import random
import time
import threading
tk=Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
count=-4
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,250,450)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    def draw(self):
        global count
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        print(pos)
        if(pos[1]<=0):
            self.y=3
        if(pos[0]<=0):
            self.x=3
        if(pos[2]>=self.canvas_width):
            self.x=-3     
        if(pos[3]>=self.canvas_height):
            self.hit_bottom=True
            canvas.create_text(250,300,text="Game Over")
            canvas.create_text(250,400,text=count)
        if(self.hit_paddle(pos)==True):
            self.y=-3
            count=count+1
        
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
             if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                 return True
        return False

            
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,450)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        global flag
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0  
    def turn_left(self,evt):
            self.x=-2
    def turn_right(self,evt):
            self.x=2
    
paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,"red")
while 1:
    if ball.hit_bottom==False :
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
            
