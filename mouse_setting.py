import numpy as np
import math
from numpy import loadtxt
from contour_data import *
import time

a = loadtxt("mouse_log0.txt",comments="#",delimiter=",",unpack=False)
inputs = np.loadtxt("input.txt",comments="#",delimiter=",",unpack=False)
#print(a[395][2])
n=a.shape[0]
images={}
flag=0
total_no_of_slide=len(inputs)
current_slide=0

slides=[]
time2=0;t=0
count_s=0;count_q=0
last_slide=0
count_spc=0
# for making column in output.txt

print("slide no, slide clicked time,     stop time,      start-time,      elapsed time on image ")

for i in range(0,n-1):
    if a[i][2]==-3:
      count_spc=count_spc+1
      #print('count_spc',count_spc)
      if count_spc==1:
         count_s=count_s+1
                                                                                                         
      if count_spc==12:   # 5 for 3 images, 12 for 10 images
         count_q=count_q+1  
    if (count_s-count_q) > 0:
      flag=flag+1
      if flag==1:
        slide_time0=a[i][3]/10000000

      if count_spc== 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11: 
 
        if a[i][2]==-3:
           
           if current_slide in slides:
             print('  '+str(a[i][3]/10000000)+',  '+str(slide_time0)+',',end= '')  # start stop time
           slide_time=a[i][3]/10000000-slide_time0
           if current_slide in slides:
             print('  '+str(slide_time))  # time elapsed on image ........................
           slide_time0=slide_time+slide_time0

           time2==0
           current_slide=current_slide+1
           #print("\n")
           
           if current_slide==total_no_of_slide+1:
              break;
              #print("\n")
                 


      if a[i][2]==2:
        #print('count_spc=',count_spc)
        #print('count_s:',count_s)
        #print('count_q:',count_q)
        
        x=a[i][0];y=a[i][1];
        #print(image1[0,0],image1[3,0], image1[1,1],image1[2,1])
        no_of_image,cords,centroid=contours_data(current_slide)
        #print('no_,cords,centroid',no_of_image,cords,centroid,'and clicked at',a[i][0],a[i][1])
        #print('no_of_image',no_of_image)
        x_axis=[];y_axis=[]
        for img in range(0,no_of_image):
             approx=cords["pic"+str(img)]
#             for j in range(len(approx)):
#                 x_axis.append(approx[j][0][0])
#                 y_axis.append(approx[j][0][1])
             x_axis=[approx[0][0][0],approx[1][0][0],approx[2][0][0]]
             y_axis=[approx[0][0][1],approx[1][0][1],approx[2][0][1]]
             min_x=min(x_axis)
             max_x=max(x_axis)
             min_y=min(y_axis)
             max_y=max(y_axis)
             if (all([x >=min_x,x<=max_x, y >=min_y, y <=max_y])):
                 if last_slide!=current_slide:  # condition for not repeating the clicks 
                     #print("\n") 
                     slides.append(current_slide)
                     print(str(current_slide)+',    '+str(a[i][3]/10000000)+',',end= '')  # clicked time
                     last_slide=current_slide

      if a[i][2]==0:
        
        x=a[i][0];y=a[i][1];
        no_of_image,cords,centroids=contours_data(current_slide)
        #print(no_of_image,cords,centroid)
       
        for im in range(0,no_of_image):
             approx=cords["pic"+str(im)]
             r=np.sqrt(np.power((centroids["cx"+str(im)]-approx[0][0][0]),2)+np.power((centroids["cy"+str(im)]-approx[0][0][1]),2))

             R=np.sqrt(np.power((centroids["cx"+str(im)]-x),2)+np.power((centroids["cy"+str(im)]-y),2))
             if (R<=(r/2)) and time2==0:
                time2=a[i][3]/10000000
                
                IMAGE1_no=str(im)
                #print('  {} ,   0                                #      you are at slide_no ,image_no'.format(current_slide,im))
             if R<(r/2) and time2!=0:
                time1=a[i][3]/1000000
                IMAGE2_no=str(im)
                time_diff=time1-time2    
                #if IMAGE1_no!=IMAGE2_no:   
                 #print(str(current_slide),end= '')
                
                IMAGE1_no=IMAGE2_no
                time2=time1


       
         

            
        
