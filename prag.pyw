from pynput.keyboard import Key, Listener
import logging
import time
#log_dir = ""

#logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.basicConfig(filename="mouse_log0.txt",level=logging.DEBUG,format=" %(message)s")


def on_press(key):
    t=str(key)
    if(t=='Key.space'):
       logging.info("0,0,-3,{}".format(int(1000000*time.time())))

         

with Listener(on_press=on_press) as listener:
    listener.join()

