# Author: Atanu Sarkar
# image capture
# v1.0
# 15-December-2020

import numpy as np
import pygame
import cv2
from _datetime import datetime

# initialize pygame
pygame.init()

# initialize opencv video capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# input video frame properties
_, frame = cap.read()
HEIGHT = frame.shape[0]
WIDTH = frame.shape[1]

# create display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("dataset creator")

# global variables
debugging_mode = False       # make this flag True to enable debugging mode
running = cap.isOpened()

capture_0 = False             # flags to check if a num keys were pressed
capture_1 = False
capture_2 = False
capture_3 = False
capture_4 = False
capture_5 = False
capture_6 = False
capture_7 = False


# Input key states (keyboard)
Key_0_Pressed = 0
Key_1_Pressed = 0
Key_2_Pressed = 0
Key_3_Pressed = 0
Key_4_Pressed = 0
Key_5_Pressed = 0
Key_6_Pressed = 0
Key_7_Pressed = 0
Q_Key_Pressed = 0
ESC_Key_Pressed = 0

# main app loop begins
while running:

    # clear last frame
    window.fill((0, 0, 0))

    # register events
    for event in pygame.event.get():
        # Quit Event
        if event.type == pygame.QUIT:
            running = False

        # Keypress Down Event
        if event.type == pygame.KEYDOWN:
            # Esc Key down
            if event.key == pygame.K_ESCAPE:
                if debugging_mode:
                    print("LOG: Escape Key Pressed Down")
                ESC_Key_Pressed = 1
            # Q Key down
            if event.key == pygame.K_q:
                if debugging_mode:
                    print("LOG: Q Key Pressed Down")
                Q_Key_Pressed = 1
            # Num 0 Key down
            if event.key == pygame.K_0:
                if debugging_mode:
                    print("LOG: Num 0 Key Pressed Down")
                Key_0_Pressed = 1
                capture_0 = True
            # Num 1 Key down
            if event.key == pygame.K_1:
                if debugging_mode:
                    print("LOG: Num 1 Key Pressed Down")
                Key_1_Pressed = 1
                capture_1 = True
            # Num 2 Key down
            if event.key == pygame.K_2:
                if debugging_mode:
                    print("LOG: Num 2 Key Pressed Down")
                Key_2_Pressed = 1
                capture_2 = True
            # Num 3 Key down
            if event.key == pygame.K_3:
                if debugging_mode:
                    print("LOG: Num 3 Key Pressed Down")
                Key_3_Pressed = 1
                capture_3 = True
            # Num 4 Key down
            if event.key == pygame.K_4:
                if debugging_mode:
                    print("LOG: Num 4 Key Pressed Down")
                Key_4_Pressed = 1
                capture_4 = True
            # Num 5 Key down
            if event.key == pygame.K_5:
                if debugging_mode:
                    print("LOG: Num 5 Key Pressed Down")
                Key_5_Pressed = 1
                capture_5 = True
            # Num 6 Key down
            if event.key == pygame.K_6:
                if debugging_mode:
                    print("LOG: Num 6 Key Pressed Down")
                Key_6_Pressed = 1
                capture_6 = True
            # Num 7 Key down
            if event.key == pygame.K_7:
                if debugging_mode:
                    print("LOG: Num 7 Key Pressed Down")
                Key_7_Pressed = 1
                capture_7 = True

        # Keypress Up Event
        if event.type == pygame.KEYUP:
            # Esc Key up
            if event.key == pygame.K_ESCAPE:
                if debugging_mode:
                    print("LOG: Escape Key Released")
                ESC_Key_Pressed = 0
            # Q Key up
            if event.key == pygame.K_q:
                if debugging_mode:
                    print("LOG: Q Key Released")
                Q_Key_Pressed = 0
            # Num 0 Key up
            if event.key == pygame.K_0:
                if debugging_mode:
                    print("LOG: Num 0 Key Released")
                Key_0_Pressed = 0
            # Num 1 Key up
            if event.key == pygame.K_1:
                if debugging_mode:
                    print("LOG: Num 1 Key Released")
                Key_1_Pressed = 0
            # Num 2 Key up
            if event.key == pygame.K_2:
                if debugging_mode:
                    print("LOG: Num 2 Key Released")
                Key_2_Pressed = 0
            # Num 3 Key up
            if event.key == pygame.K_3:
                if debugging_mode:
                    print("LOG: Num 3 Key Released")
                Key_3_Pressed = 0
            # Num 4 Key up
            if event.key == pygame.K_4:
                if debugging_mode:
                    print("LOG: Num 4 Key Released")
                Key_4_Pressed = 0
            # Num 5 Key up
            if event.key == pygame.K_5:
                if debugging_mode:
                    print("LOG: Num 5 Key Released")
                Key_5_Pressed = 0
            # Num 6 Key up
            if event.key == pygame.K_6:
                if debugging_mode:
                    print("LOG: Num 6 Key Released")
                Key_6_Pressed = 0
            # Num 7 Key up
            if event.key == pygame.K_7:
                if debugging_mode:
                    print("LOG: Num 7 Key Released")
                Key_7_Pressed = 0

    # manual exit/quit app
    if Q_Key_Pressed or ESC_Key_Pressed:
        running = False

    # read frame
    ret, frame = cap.read()             # frame shape -> (480, 640, 3)

    # check for image capture event and save image into dataset
    # class 0
    if Key_0_Pressed == 0 and capture_0:
        capture_0 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_0/")
        filename = str("IMG" + "_c0_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 1
    if Key_1_Pressed == 0 and capture_1:
        capture_1 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_1/")
        filename = str("IMG" + "_c1_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 2
    if Key_2_Pressed == 0 and capture_2:
        capture_2 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_2/")
        filename = str("IMG" + "_c2_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 3
    if Key_3_Pressed == 0 and capture_3:
        capture_3 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_3/")
        filename = str("IMG" + "_c3_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 4
    if Key_4_Pressed == 0 and capture_4:
        capture_4 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_4/")
        filename = str("IMG" + "_c4_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 5
    if Key_5_Pressed == 0 and capture_5:
        capture_5 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_5/")
        filename = str("IMG" + "_c5_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 6
    if Key_6_Pressed == 0 and capture_6:
        capture_6 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_6/")
        filename = str("IMG" + "_c6_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")
    # class 7
    if Key_7_Pressed == 0 and capture_7:
        capture_7 = False
        image = frame[40:440, 120:520, :].copy()
        timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        path = str("data/class_7/")
        filename = str("IMG" + "_c7_" + timestamp + ".png")
        cv2.imwrite(path + filename, image)
        print("LOG: " + filename + " Saved to " + path + "successfully!!")

    # frame shape -> (480, 640, 3)
    frame = cv2.rectangle(frame, (120, 40), (520, 440), (0, 0, 255), 5)

    # opencv view (for debugging)
    if debugging_mode:
        cv2.imshow("opencv", frame)

    # convert to pygame surface
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # blit the frame
    window.blit(frame, (0, 0))

    # render the display
    pygame.display.update()


# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
pygame.quit()

