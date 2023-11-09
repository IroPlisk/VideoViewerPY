import cv2 #serve la libreria CV2 per questo programma, senza non funziona
import os
import random

videofolderPath = './videos'
videos = []
playlist = []
for file in os.listdir(videofolderPath):
    if file.lower().endswith(".mp4"):
        path = os.path.join(videofolderPath, file)
        playlist.append(path)


for i in range(3):
    cap = cv2.VideoCapture(playlist[i])
    print(playlist[i])

    while True:
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
            cap.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame', frame)
    cap.release()
    cv2.destroyAllWindows()

    i += 1 # UPDATE INDICE