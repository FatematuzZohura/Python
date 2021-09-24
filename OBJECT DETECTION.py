import cv2
cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()
success,img =cap.read()
bbx =cv2.selectROI("Tracker fps",img,False)
tracker.init(img,bbx)
def drawbox(img,bbx):
    x,y,w,h = int(bbx[0]),int(bbx[1]),int(bbx[2]),int(bbx[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(225,0,225),3,1)
    cv2.putText(img,"tracker",(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
while True:
    time = cv2.getTickCount()
    success,img=cap.read()
    success,bbx= tracker.update(img)
    print(bbx)
    if success:
        drawbox(img,bbx)
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-time)
    cv2.putText(img,str(int(fps)),(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
    cv2.imshow("Tracking img",img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
