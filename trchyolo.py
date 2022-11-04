import torch 
import numpy as np
import cv2
import matplotlib.pyplot as plt
import uuid
import os
import time
import random
import subprocess
import pyttsx3
from shutil import copyfile

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp2/weights/last.pt', force_reload=True)


# A countdown function but not used in code
# It was an idea to use a countdown system for a the alarm logic
# def countdown(t):
#     # A countdown timer func
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#     print('Fire in the hole!!')

# Function to play a random music from our chosen directory
def play_music():
    dst_path = r'C:\Users\LENOVO\Desktop\Izu\AdvProjects\music.mp3'
    music_file = random.choice(os.listdir(r"C:\Users\LENOVO\Music\Music"))
    src_file =  r'C:\Users\LENOVO\Music\Music' + f'\{music_file}'
    music_file = copyfile(src_file, dst_path )
    player_path = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
    subprocess.call([player_path, music_file])

# Function to play Text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# img = os.path.join('data', 'images', 'Awake.3a6d4646-5b68-11ed-bc50-68f72886fc79.jpg')
# results = model(img)
# df = results.pandas().xyxy[0]
# print(df)
# y = df['name'].values
# print(y)

awake = 0
drowsy = 0
cap = cv2.VideoCapture(0)
while cap.isOpened():
    word = 'Focus!!!'
    ret, frame = cap.read()
    # Make detections 
    results = model(frame)
    # making sure our results are not empty
    df = results.pandas().xyxy[0]
    if not df.empty:
        y = df['name'].values[0]  

        # Our Alarm logic###########
        if y == 'Awake' or y == 'Drowsy':
            if y=='Awake':
                awake+=1
                if awake>15:
                    word = "Nice Going, Stay Focused!!!"
                    speak(word)
                    awake=0
                    # if awake>30:
                    #     awake=0
            if y=='Drowsy':
                drowsy+=1
                if drowsy>10:
                    word = "Focus Sleepy head!!!"
                    if drowsy>15:
                        speak(word*2)
                        if drowsy>25:
                            play_music()
                            if drowsy>30:
                                drowsy=0
            #######################
            # Shows y state (Awake or Drowsy)
            print(y)
    else:
        print('No Detection')
    
    cv2.putText(frame, word, (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()