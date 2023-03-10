import cv2
frameWidth = 640
frameHeight = 480

nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,0)
count = 0
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()           # That's to read the cap or the webcam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplates = nPlateCascade.detectMultiScale(gray, 1.1, 10)
    for (x,y,w,h) in nplates:
        area = w*h
        if area > minArea:

            cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0),3)
            cv2.putText(img,"Number Plate", (x, y-h), cv2.FONT_HERSHEY_DUPLEX, 1, color, 3)
            imgRegion = img[y:y+h, x:x+w]
            cv2.imshow("ImageRegion", imgRegion)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jbg", imgRegion)
        cv2.rectangle(img, (0,200), (640,300), (255,0,250), cv2.FILLED)
        cv2.putText(img, "Scan saved", (150,265), cv2.FONT_HERSHEY_TRIPLEX,1, (0,0,255), 2)
        cv2.imshow("Video", img)
        cv2.waitKey(0)
        count += 1
