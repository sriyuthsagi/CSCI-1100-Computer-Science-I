from tkinter import *


class Ball(object):
    def __init__ (self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        
        
        
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    
    def bounding_box(self):
        return (self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        return 0 < self.x + self.radius and self.x - self.radius < maxx and 0 < self.y + self.radius and self.y - self.radius < maxy
    
    def check_and_reverse(self, maxx, maxy):
        if self.x - self.radius < 0 or self.x + self.radius > maxx:
            self.dx = -self.dx
        
        if self.y - self.radius < 0 or self.y + self.radius > maxy:
            self.dy = -self.dy               
        
        
        
        
        
"""
        self.ball_x,self.ball_y = 0,400
        self.ball_radius = 10
        self.ball_dx,self.ball_dy = 6,-10
        self.ball_color = "green"
        self.wait_time = 100 
        self.isstopped = False 
        self.maxx = 400
        self.maxy = 400        
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)        
"""



if __name__ == "__main__":
    root = Tk()
    bd = Ball(0, 400, 6, -10, 10, 'green')
