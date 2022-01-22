

#------------
import keyword
import pyautogui
from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss
import uuid
"""
Game
https://gamaverse.com/parkour-run-game/
"""

mon = {
    "top": 325,
    "left": 245,
    "width": 311,
    "height": 292
}
sct=mss()

width=125
height=50

model=model_from_json(open("model.json","r").read())
model.load_weights("model.h5")
# down = 0, right = 1, up = 2

labels = ["down","up","right"]

while True:

    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im2 = np.array(im.convert("L").resize((width, height)))
    im2 = im2 / 255

    X = np.array([im2])
    X = X.reshape(X.shape[0], width, height, 1)
    r = model.predict(X)
    #keyboard.press(keyboard.KEY_DOWN)
    result = np.argmax(r)

    if result ==0:
        pyautogui.keyDown("down")
        time.sleep(1.1)
        pyautogui.keyUp("down")
        #pyautogui.press("down")



        print( "prediction is down")




    elif result == 1:

        pyautogui.press('right')


        print("prediction is right")



    elif result ==2:
        pyautogui.keyDown('up')
        time.sleep(0.3)
        pyautogui.keyUp('up')
        #pyautogui.press('up')
        print("prediction is up")




















