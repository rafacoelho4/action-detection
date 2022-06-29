# -*- coding: utf-8 -*-
"""MotionDetection.ipynb

# Maria Laura
"""

import cv2
# from google.colab.patches import cv2_imshow
import numpy as np

cap = cv2.VideoCapture(0)#carregar vídeo

ret, frame1 = cap.read() #lendo o 1 frame
ret, frame2 = cap.read() #lendo o 2 frame

while True:  
  diff = cv2.absdiff(frame1,frame2) #pegando a diferença absoluta entre os frames
  cv2.imshow("Motion Detection", diff)
  gray = cv2.cvtColor( diff, cv2.COLOR_BGR2GRAY) #tranformando a diferença em escala de cinza
  # cv2.imshow("Motion Detection", gray)
  blur = cv2.GaussianBlur(gray,(5,5), 0) #aplicar o desfoque gaussiano na variavel que contem a diferença em escala de cinza
  # cv2.imshow("Motion Detection", blur)
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)#encontrar o threshhold
  # cv2.imshow("Motion Detection", thresh)
  dilated = cv2.dilate(thresh, None, iterations=4) #dilatar a imagem para preencher todas as lacunas e ajudar a reconhecer os melhores contornos
  # cv2.imshow("Motion Detection", dilated)
  contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #criando os contornos para imagem dilatada

  #criando contornos
  for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour) < 3000:
      continue
    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

  cv2.imshow("Motion Detection", frame1)

  frame1 = frame2
  ret, frame2 = cap.read()

  if ret == False:
    break

  key = cv2.waitKey(1)
  if key == ord('q'):
    break


cap.release()
# out.release()
