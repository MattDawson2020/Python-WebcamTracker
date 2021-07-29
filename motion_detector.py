import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[]
times=[]
df=pandas.DataFrame(columns=['Start', 'End'])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    status = 0

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
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h)=cv2.boundingRect(contour)
        #if the contour within the frame is large enough, apply the rectancle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
    status_list.append(status)

    # status_list=status_list[-2:]

    #record the status changes (when movement enters frame) and append to the list
    # the following loop checks for when movement enters or leave the screens and records timestamps
    if len(status_list) > 1:
        if status_list[-1]==1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1]==0 and status_list[-2] == 1:
            times.append(datetime.now())

    # cv2.imshow("Capturing", gray)
    # cv2.imshow("Delta Frame", delta_frame) #lets you see the difference between initial frame and current one 
    # cv2.imshow("threshhold frame", thresh_frame) # lets you see the frames in binary colors, white for movement black for nothing
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
            # adds a closing none movement value if the loop is broken during motion
        break

for i in range(0, len(times), 2):
    df=df.append({'Start': times[i], 'End': times[i + 1]}, ignore_index=True)
#iterate through the times list in steps of two, and adds the start and end times of motion

df.to_csv("Times.csv")
# store the times on a csv

video.release()
cv2.destroyAllWindows