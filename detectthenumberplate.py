import cv2

cap=cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,720)
number_cancade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
skip =0

while(cap.isOpened()):
    ret , frame =cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==False:
        continue
    number=number_cancade.detectMultiScale(gray,1.1,5)
    # if len(number)==0:
    #     continue
    k=1
    number=sorted(number,key=lambda x: x[2]*x[3],reverse=True)
    skip +=1
    i=0
    for numbers in number:
        x,y,w,h =numbers
        offset=5
        number_offset=frame[y-offset :y+offset,x-offset:x+offset]
        # number_selection=cv2.resize(number_offset,[1000,1000])
        # cv2.imshow(str(k),number_selection)
        k+=1
        img1=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        gray_plates=gray[y:y+h,x:x+w]
        cv2.imwrite(f"numberplate{i}.jpg",gray_plates)
        cv2.imwrite(f"numberplatedetect.jpg",img1)
        cv2.imshow("number plte",gray_plates)
        i=i+1
    cv2.imshow("number plate detection",frame)
    frame=cap.read()

    if cv2.waitKey(27) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()