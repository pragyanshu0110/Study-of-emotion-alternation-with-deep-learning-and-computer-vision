import os
import time
import pandas as pd

df3=pd.read_csv('input_s_and_t.txt', sep=',',comment='#',header=None)
sub_id=(df3[2][0])

dirName = 'final_outputs/'+str(sub_id) 

if not os.path.exists(dirName):
	os.mkdir(dirName)

os.system("python3 only.py")

if __name__ == '__main__':
    os.chdir("/home/iiitg_rd/prag/mouse_final_proj_copy_for_trial_1/face_classification-master/src")
    os.system('gnome-terminal -x sh -c "python3 video_emotion_color_demo.py; bash"')
    time.sleep(5) # sleep time for showing image after camera is on
    os.system('gnome-terminal -x sh -c "python3 show_image.py; bash"')
