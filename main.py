import threading
from functools import partial
from kivy.app import App
from kivy.uix import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import numpy as np
import imutils
import socket 



host = "192.168.4.1"  #ESP32 IP in local network
port = 80             #ESP32 Server Port 

Window.size=(400,600)
Window.clearcolor=(0,50/255,150/255,10)



#ca = "http://192.168.4.3:8080/video"

#global sa


def ttr(s):
    if s=='U':
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(s.encode('utf-8'))
        sock.close()
        
    elif s=='R':
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(s.encode('utf-8'))
        sock.close()
    elif s=='L':
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(s.encode('utf-8'))
        sock.close()
    elif s=='B':
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(s.encode('utf-8'))
        sock.close()
    elif s=='S':
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(s.encode('utf-8'))
        sock.close()





class FirstW(Screen):
    pass


class SecundW(Screen):

    pass


class TherdW(Screen):
    
    pass




class MainW(ScreenManager):
    pass

ka = Builder.load_file("control.kv")

class Control(App):
    d=0
    
    
    def build(self):
        self.title = "Control App"
        threading.Thread(target=self.doit, daemon=True).start()
        
       
        
        #self.new_screen = TherdW()
        self.new_screen = SecundW()
        return ka
    
    
    def tr(self,s):
        if s=='u':
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(s.encode('utf-8'))
            sock.close()
            
        elif s=='r':
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(s.encode('utf-8'))
            sock.close()
        elif s=='l':
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(s.encode('utf-8'))
            sock.close()
        elif s=='b':
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(s.encode('utf-8'))
            sock.close()
        elif s=='s':
            sock = socket.socket()
            sock.connect((host, port))
            sock.send(s.encode('utf-8'))
            sock.close()
        
        
        
    ip=""    
    def getTextInput(self,text):
        global ip 
        ip=text
        print(ip)
        
    
        
        

    def dis(self):
        self.d=1
    def ena(self):
        self.d=0
        
    
    def doit(self):
        # this code is run in a separate thread
        self.do_vid = False  # flag to stop loop

        # make a window for use by cv2
        # flags allow resizing without regard to aspect ratio
        #cv2.namedWindow('Hidden', cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

        # resize the window to (0,0) to make it invisible
        #cv2.resizeWindow('Hidden', 0, 0)
        
        
        

        while True:
            # start processing loop
            
             
            while (self.do_vid):
                cam = cv2.VideoCapture(ip) 
                print(ip)
                ret, frame = cam.read()
                # ...
                # more code
                # ...
                if self.d==0: 
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    
                    lower_yellow = np.array([20, 100, 100])
                    upper_yellow = np.array([30, 255, 255])
                    
                    lower_green = np.array([50, 100,100])
                    upper_green = np.array([70, 255, 255])
                    
                    lower_red = np.array([156,161,255])
                    upper_red = np.array([30,0,255])
                    
                    lower_blue = np.array([98,50,50])
                    upper_blue = np.array([139,255,255])
                    
                    
                    
                    
                    mask1 = cv2.inRange(hsv, lower_yellow,upper_yellow)
                    mask2 = cv2.inRange(hsv, lower_green,upper_green)
                    mask3 = cv2.inRange(hsv, lower_red,upper_red)
                    mask4 = cv2.inRange(hsv, lower_blue,upper_blue)
                    
                    cnts1 = cv2.findContours(mask1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    cnts1 = imutils.grab_contours(cnts1)
                    
                    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    cnts2 = imutils.grab_contours(cnts2)
                    
                    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    cnts3 = imutils.grab_contours(cnts3)
                    
                    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    cnts4 = imutils.grab_contours(cnts4)
                    
                    
                    for c in cnts1:
                        area1 = cv2.contourArea(c)
                        if area1 > 5000 :
                            cv2.drawContours(frame, [c],-1,(0,255,0),3)
                            ttr('U')
                            M = cv2.moments(c)
                            cx = int(M["m10"]/M["m00"])
                            cy = int(M["m01"]/M["m00"])
                            
                            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
                            cv2.putText(frame,"Yellow",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),1)
                            
                    for c in cnts2:
                        area2 = cv2.contourArea(c)
                        if area2 > 5000 :
                            cv2.drawContours(frame, [c],-1,(0,255,0),3)
                            ttr('L')
                            
                            M = cv2.moments(c)
                            cx = int(M["m10"]/M["m00"])
                            cy = int(M["m01"]/M["m00"])
                            
                            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
                            cv2.putText(frame,"Green",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),1)
                            
                    for c in cnts3:
                        area3 = cv2.contourArea(c)
                        if area3 > 5000 :
                            cv2.drawContours(frame, [c],-1,(0,255,0),3)
                            
                            ttr('B')
                            
                            M = cv2.moments(c)
                            cx = int(M["m10"]/M["m00"])
                            cy = int(M["m01"]/M["m00"])
                            
                            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
                            cv2.putText(frame,"Red",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),1)
                            
                            
                    for c in cnts4:
                        area4 = cv2.contourArea(c)
                        if area4 > 5000 :
                            cv2.drawContours(frame, [c],-1,(0,255,0),3)
                            
                            ttr('R')
                            
                            
                            
                            M = cv2.moments(c)
                            cx = int(M["m10"]/M["m00"])
                            cy = int(M["m01"]/M["m00"])
                            
                            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
                            cv2.putText(frame,"Blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),1)

                
                # send this frame to the kivy Image Widget
                # Must use Clock.schedule_once to get this bit of code
                # to run back on the main thread (required for GUI operations)
                # the partial function just says to call the specified method with the provided argument (Clock adds a time argument)
                Clock.schedule_once(partial(self.display_frame, frame))
                
     
                #cv2.imshow('Hidden', frame)
                #cv2.waitKey(1)
            #cam.release()
            #cv2.destroyAllWindows()
                
                    
                    
                
    
   
        
      
            
       
        
        
        
        
        
    def run_vid(self):
        # stop the video capture loop
        self.do_vid = True
    def stop_vid(self):
        # stop the video capture loop
        self.do_vid = False

    def display_frame(self, frame, dt):
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(frame.tobytes(order=None), colorfmt='bgr', bufferfmt='ubyte')
        texture.flip_vertical()

        # No output of the Video Stream
        # Scan().ids.vid.texture = texture also doesn't work
       # self.new_screen.ids.vid.texture = texture
        self.root.get_screen('three').ids.vid.texture = texture
        self.root.get_screen('tow').ids.vid.texture = texture
    
    
  
if __name__ == '__main__':
    Control().run();
    


