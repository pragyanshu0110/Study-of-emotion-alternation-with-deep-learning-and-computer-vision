from pynput.mouse import Listener

def on_move(x,y):
    print("mouse moved to ({},{})".format(x,y))
    


def on_click(x,y,button,pressed):
    print("mouse clicked at ({},{}) with {}".format(x,y,button))


def on_scroll(x,y,dx,dy):
    print("mouse scrolled AT ({},{})  ({},{})".format(x,y,dx,dy))

with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()
