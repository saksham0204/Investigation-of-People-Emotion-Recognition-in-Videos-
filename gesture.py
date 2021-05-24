#  this file is created to capture the face and build the dataset
#   Saksham Gera (all rights are reserved)
import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data2"):
    os.makedirs("data2")
    os.makedirs("data2/train")
    os.makedirs("data2/test")
    os.makedirs("data2/train/0")
    os.makedirs("data2/train/1")
    os.makedirs("data2/train/2")
    os.makedirs("data2/train/3")
    os.makedirs("data2/train/4")

    os.makedirs("data2/test/0")
    os.makedirs("data2/test/1")
    os.makedirs("data2/test/2")
    os.makedirs("data2/test/3")
    os.makedirs("data2/test/4")


# Train or test
mode = 'train'
directory = 'data2/' + mode + '/'

cap = cv2.VideoCapture(0)  # initilizing the webacam

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    # Getting count of existing images
    count = {'zero': len(os.listdir(directory + "/0")),
             'one': len(os.listdir(directory + "/1")),
             'two': len(os.listdir(directory + "/2")),
             'three': len(os.listdir(directory + "/3")),
             'four': len(os.listdir(directory + "/4"))
             }
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "happy : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "sad : " + str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "angry : " + str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "surprise : " + str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "neutral : " + str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))

    cv2.imshow("Frame", frame)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(count['zero']) + '.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory + '1/' + str(count['one']) + '.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory + '2/' + str(count['two']) + '.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory + '3/' + str(count['three']) + '.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory + '4/' + str(count['four']) + '.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory + '5/' + str(count['five']) + '.jpg', roi)
cap.release()
cv2.destroyAllWindows()
