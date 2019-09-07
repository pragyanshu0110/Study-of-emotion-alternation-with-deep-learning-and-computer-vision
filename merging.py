'''this file merging the output.csv and emo_out.csv'''
import os
import pandas as pd

# reading output.txt file
df=pd.read_csv('output.csv', sep=',',header=None)
n=len(df)

# reading emo_out.txt file
df2=pd.read_csv('emo_out.csv', sep=',',header=None)
m=len(df2)
i=1

df3=pd.read_csv('input_s_and_t.txt', sep=',',comment='#',header=None)
session=(df3[0][0])
trial=(df3[1][0])
ID_no=(df3[2][0])


#=============================================================================

# this section for the image description

df3=pd.read_csv('s'+str(session)+'/t'+str(trial)+'/'+'rating.csv', sep=',',header=None)

A=pd.read_csv('image_sequence.csv', sep=',',header=None)

#=============================================================================


save_path = '/home/iiitg_rd/prag/mouse_final_proj_copy_for_trial_1/final_outputs/'+str(ID_no)
name_of_file = str(ID_no)+'_'+str(session)+'_'+str(trial)

completeName = os.path.join(save_path, name_of_file+".txt")         
f = open(completeName, "w")

#f = open('final_emo_out.txt','w')         #========= opening the file write mode == 
f.write('#slide_no, emotion_on_click,     avg_emo,      elapsed_time,               image_description,          image_no,           valence_mean(SD),         arousal_mean(SD)'+'\n')
while i < n:#i<n
        t=A[0][i-1]
        image_description=df3[0][t-1]
        image_no=df3[1][t-1]
        valence_mean=df3[2][t-1]
        arousal_mean=df3[3][t-1]


        elapsed_time=(df[4][i])
        start_time=(df[3][i])
        stop_time=(df[2][i])
        clicked_time=format(float(df[1][i]),".2f")
        #print(str(clicked_time)+'cli_time')
        j=0;emotion=0;emo_on_click=0
        while j < m-1:# j  < m-1
              current_time=(df2[1][j])
              current_time2=format(float(df2[1][j]),".2f")
              #print(str(current_time2)+'curr time')
              if float(clicked_time)==float(current_time2):
                 emo_on_click=df2[0][j]+emo_on_click
              if float(start_time) <= float(current_time) and float(current_time) <= float(stop_time):
                   emotion=df2[0][j]+emotion
              j=j+1             
        if emo_on_click > 1:
           emo_on_click=1
        if emo_on_click < -1:
           emo_on_click=-1
        f.write(str(i)+',             '+str(emo_on_click)+',                    '+str(emotion)+',        '+str(elapsed_time)+',        '+str(image_description)+',                        '+str(image_no)+',                  '+str(valence_mean)+',               '+str(arousal_mean)+"\n")      # write in file
        i=i+1

