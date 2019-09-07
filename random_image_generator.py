from __future__ import print_function

import pandas as pd
import os
import numpy as np
from PIL import Image
import glob
import cv2
import random
import sys
# SIZE OF SCREEN OF PC/LAPTOP
X_CORD=1919
Y_CORD=1079

In_text=pd.read_csv('input_s_and_t.txt', sep=',',comment='#',header=None)
session=In_text[0][0]
#print(In_text.shape)
trial=In_text[1][0]
ID_no=In_text[2][0]
#print(session)
#print(trial)
#print(ID_no)
t1=1
t2=1
inputs = np.loadtxt("input.txt",comments="#",delimiter=",",unpack=False)
images=[]
for r in range(1,len(inputs)+1):

  #N=int(input("how many iamges you want to take folder"))
  N=int(inputs[r-1][1])
  
  for m in range(N):
      #------- tagging folder names 
    
   
      #------ read images from input folder
      if r==1:
        filenames = glob.glob('s'+str(session)+'/t'+str(trial)+"/*.jpg")
        filenames.sort()             # reading images sequentially from folder
        images = [cv2.imread(file) for file in filenames]  
         
      #print(images[0])

      #------- save images in  output folder
      outpath='outsad'

      l=len(images)
      #print('l=',l)

      if r==1:   
          data=random.sample(range(1,l+1),l)
      #print('len=',len(data))
      #print('data[r-1]',data[r-1])  
      print(data[r-1])
      sys.stdout.flush()    
      cv2.imwrite(os.path.join(outpath,str(m+1)+'.jpg'),images[data[r-1]-1])  
        
      
  files = []
  for k in range(N):       
      files.append('outsad/'+str(k+1)+'.jpg')

  size_x=800;size_y=800
  result = Image.new("RGB", (X_CORD,Y_CORD),(255,255,255))

  p=(size_x*size_y//(N*1.8))
  #print('p=',p)
  s=int(np.sqrt(p))
  #print('s=',s)
  t=0
  #x=180
  #y=150
  w=0;h=0
  a=0;b=0
  max_a=a 
  max_b=b
  for index, file in enumerate(files):
     #print(index,file)
     path = os.path.expanduser(file)
     img = Image.open(path)
 
     random_no=np.random.randint(0,2)
     
     if random_no==0:
        #print('imagefrom====0')
        x=180;y=150
        a=np.random.randint(1200,1300)
        b=np.random.randint(800,900)
	
     if random_no==1:
        #print('imagefrom====1')
        y=40;x=200
        a=np.random.randint(1400,1600)
        b=np.random.randint(800,850)
     

     img = img.resize((a,b), Image.BILINEAR)

     x = x  + max_a +30 #index // (N//3) * s  # t is for gap between the images
     y = y    #index % (N//3) * s 
     w, h = img.size

     if a>max_a:
       max_a=a
     if b>max_b:
       max_b=b

     if x+w > X_CORD:
       x=30
       y=y+max_b+30
     #print('pos {0},{1}    w,h: {2},{3}   size:{4}'.format(x, y, w, h,img.size))  
     result.paste(img, (x, y, x + w, y + h))

     t=t+20
  result.save(os.path.expanduser('~/prag/mouse_final_proj_copy_for_trial_1/'+str(r)+ '.jpg'))
  result.save(os.path.expanduser('~/prag/mouse_final_proj_copy_for_trial_1/face_classification-master/src/'+str(r)+ '.jpg'))
 

