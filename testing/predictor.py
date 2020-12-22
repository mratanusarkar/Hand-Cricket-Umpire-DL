# Author: Atanu Sarkar
# predictor
# v1.0
# 21-December-2020

import numpy as np
import pygame
import cv2
import tensorflow as tf

# user input variables
DEBUGGING_MODE = True          # make this flag True to enable debugging mode
USE_CAMERA_NUMBER = 1           # default is 0
FLIP_CAMERA = True             # to flip camera horizontally
SIDE = 256                      # side length (in px) of the capture image for the dataset
MODEL_PATH = "models/1608545816.h5"

# initialize pygame
pygame.init()

# initialize opencv video capture
cap = cv2.VideoCapture(USE_CAMERA_NUMBER, cv2.CAP_DSHOW)

# input video frame properties
_, frame = cap.read()           # (480, 640, 3)
HEIGHT = frame.shape[0]
WIDTH = frame.shape[1]

# create display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("predictor")

# global variables
running = cap.isOpened()

x1 = int((WIDTH - SIDE) / 2)    # x1, x2, y1, y2 are the coordinates of capture square
x2 = int((WIDTH + SIDE) / 2)
y1 = int((HEIGHT - SIDE) / 2)
y2 = int((HEIGHT + SIDE) / 2)

rect_color = (255, 0, 0)

# Input key states (keyboard)
Q_Key_Pressed = 0
ESC_Key_Pressed = 0

if DEBUGGING_MODE:
    print("Window Size: " + str(WIDTH) + " x " + str(HEIGHT) + "  (in px)")

# load TF model
model = tf.keras.models.load_model("models/1608545816.h5")
if DEBUGGING_MODE:
    print(model.summary())

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
                if DEBUGGING_MODE:
                    print("LOG: Escape Key Pressed Down")
                ESC_Key_Pressed = 1
            # Q Key down
            if event.key == pygame.K_q:
                if DEBUGGING_MODE:
                    print("LOG: Q Key Pressed Down")
                Q_Key_Pressed = 1
        # Keypress Up Event
        if event.type == pygame.KEYUP:
            # Esc Key up
            if event.key == pygame.K_ESCAPE:
                if DEBUGGING_MODE:
                    print("LOG: Escape Key Released")
                ESC_Key_Pressed = 0
            # Q Key up
            if event.key == pygame.K_q:
                if DEBUGGING_MODE:
                    print("LOG: Q Key Released")
                Q_Key_Pressed = 0

    # manual exit/quit app
    if Q_Key_Pressed or ESC_Key_Pressed:
        running = False

    # read frame
    ret, frame = cap.read()             # frame shape -> (480, 640, 3)

    # flip image frame if FLIP_CAMERA
    if FLIP_CAMERA:
        frame = cv2.flip(frame, 1)

    # predict using the TF model
    img = frame[y1:y2, x1:x2, :]
    img = np.expand_dims(img, axis=0)
    prediction = np.argmax(model.predict(img))
    print(prediction)

    # opencv view (for debugging)
    if DEBUGGING_MODE:
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
        cv2.imshow("opencv", frame)

    # convert to pygame surface
    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # blit the frame
    window.blit(frame, (0, 0))

    # blit square frame to indicate the capture area
    pygame.draw.rect(window, rect_color, (x1, y1, SIDE, SIDE), 5)

    # render the display
    pygame.display.update()


# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
pygame.quit()
