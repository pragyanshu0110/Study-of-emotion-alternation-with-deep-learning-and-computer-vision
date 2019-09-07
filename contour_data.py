import cv2
import numpy as np

def contours_data(image_num):
     img=cv2.imread(str(image_num)+'.jpg')
     blurred_img=cv2.GaussianBlur(img,(15,15),0)
     gray=cv2.cvtColor(blurred_img,cv2.COLOR_BGR2GRAY)
     ret,thresholded=cv2.threshold(gray,250,255,0)
     img2,contours,hierarchy = cv2.findContours(thresholded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     k=1
     #cv2.drawContours(img,contours,-1,(0,0,255),2)
     centroids={}
     cords={}
     #cv2.imshow('contour',img)
     #cv2.waitKey(0)
     no_of_img=0

     i=0
     while True:
         cnt=contours[k]
         count1=0;count2=0
         #APPROXIMATION
         approx=cv2.approxPolyDP(cnt,0.135*cv2.arcLength(cnt,True),True)

         if len(approx)==3:
               l1=abs(approx[0][0][0]-approx[1][0][0])
               l2=abs(approx[1][0][0]-approx[2][0][0])
               l3=abs(approx[0][0][0]-approx[2][0][0])
      
               if l1 > 20 and l2> 20 and l3>20:
                  count1=1
                  count2=2
         #print(approx)
         #print('aaa',approx[0][0][0],approx[1][0][0],approx[2][0][0],'end')




         if len(approx)>=(4-count1):
           if (4-count1)==4:           

              if abs(approx[0][0][0]-approx[1][0][0]) < 20:
                  count2=count2+1
              if abs(approx[0][0][0]-approx[2][0][0]) < 20:
                  count2=count2+1
              if abs(approx[0][0][0]-approx[3][0][0]) < 20:
                  count2=count2+1

           if count2 < 2: 
             #cv2.drawContours(img,contours,k,(0,0,255),2)
             #cv2.imshow("contour",img)
             #cv2.waitKey(0)
             no_of_img=1+no_of_img
   
             #print('aaa',approx[0][0][0],approx[1][0][0],approx[2][0][0],'end')
             cords["pic"+str(i)]=approx         
             
             #cv2.imshow('contour',img)
             #cv2.waitKey(0)

             M=cv2.moments(cnt)
	     #print('moments',M)
             ####  CENTEROID
             cx=int(M['m10']/M['m00'])
             cy=int(M['m01']/M['m00'])
             centroids["cx"+str(i)]=cx
             centroids["cy"+str(i)]=cy
             #print('centroid is:', '(',cx,',',cy,')')
             i=i+1
    
         k=k+1
         if k==len(contours):
             break

     return no_of_img,cords,centroids

#arr=[3,4,5]
#for r in arr:
#   no_of_img,cords,center=contours_data(r)
#   print("no_of_img",no_of_img)
#   print("coordinates",cords)
#   print("centroid",center)

