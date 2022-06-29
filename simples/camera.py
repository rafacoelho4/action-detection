import cv2, time

from cv2 import threshold

# using webcam: 0
video = cv2.VideoCapture(0)

# frame 
first_frame = None

# infinite loop
while True:
    check, frame = video.read()
    # extract into grayscale: improves the accuracy of motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blurring/smoothing image
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    # the first frame is the reference frame
    if first_frame is None:
        first_frame = gray
        continue
    # calculating the absolite difference between frames
    delta_frame = cv2.absdiff(first_frame, gray)
    # limit up to wich we want the motion to be detected
    # threshold(frame, intensity, color shade, object)[first element]
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    # apply smoothing
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)
    # finding contours of objects that are moving
    (cntr, h) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # garanteeing that small noises wont be detected as contours
    for contour in cntr:
        if cv2.contourArea(contour) < 3000:
            continue
        # starting x, starting y, width and height 
        (x, y, w, h) = cv2.boundingRect(contour)
        # drawing rectangle (frame, axis, color, size of pen)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    # showing video to user
    cv2.imshow("Motion Detection", frame)
    # exit criteria for window
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
# closing all windows
cv2.destroyAllWindows()