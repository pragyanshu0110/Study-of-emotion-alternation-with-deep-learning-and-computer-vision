''' this file save(in file mouse_log0.txt) the input log from the mouse and keyboard'''
from pynput.mouse import Listener
import logging
import time
#logging.basicConfig(filename="mouse_log0.txt",level=logging.DEBUG,format="%(asctime)s: %(message)s")
logging.basicConfig(filename="mouse_log0.txt",level=logging.DEBUG,format=" %(message)s")


def on_move(x,y):
    logging.info("{},{},0,{}".format(x,y,int(1000000*time.time())))
    
def on_click(x,y,button,pressed):
    if pressed:
        t=str(button)
        if(t=='Button.left'):
            logging.info("{},{},2,{}".format(x,y,int(1000000*time.time())))
        elif(t=='Button.right'):
            logging.info("{},{},-2,{}".format(x,y,int(1000000*time.time())))

            
    
def on_scroll(x,y,dx,dy):
    logging.info("{},{},{},{}".format(x,y,dy,int(1000000*time.time())))





with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()
