import cv2, time

first_frame=None

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21), 0)
    #blurs the frame to remove noise, improves motion detector accuracy

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame, gray)
    #finds the diff between first and second frames
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #polarizes the color so you can see movement
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) # removes the excess whitespace

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #finds the contours in the frame

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        
        (x, y, w, h)=cv2.boundingRect(contour)
        #if the contour within the frame is large enough, apply the rectancle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            

    # cv2.imshow("Capturing", gray)
    # cv2.imshow("Delta Frame", delta_frame) #lets you see the difference between initial frame and current one 
    # cv2.imshow("threshhold frame", thresh_frame) # lets you see the frames in binary colors, white for movement black for nothing
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows