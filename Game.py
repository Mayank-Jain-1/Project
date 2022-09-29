import pygame 
import cv2
import numpy as np
import mediapipe as mp 
from keras.models import load_model 
import random

def inFrame(lst):
	if lst[28].visibility > 0.6 and lst[27].visibility > 0.6 and lst[15].visibility>0.6 and lst[16].visibility>0.6:
		return True 
	return False


pygame.init()
model  = load_model("model.h5")
label = np.load("labels.npy")
holistic = mp.solutions.pose
holis = holistic.Pose()
drawing = mp.solutions.drawing_utils


width, height = 640 , 360
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hole in the Screen")


fps = 30
clock = pygame.time.Clock()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,360)

imgTpose = pygame.image.load('JustSketchMe - Screenshot.png').convert_alpha()


#game variables
score = 0
highscore = 0


start = True
change = True
current_pose = "Nothing"
while start:

  if change:
    current_pose = label[random.randint(0,len(label) - 1)]
    print("The current pose is: ", current_pose)
    change = False
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      start = False
      pygame.quit()

  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  imgRGB = np.rot90(imgRGB)
  frame = pygame.surfarray.make_surface(imgRGB).convert()
  window.blit(frame,  (0,0))


  # print(label)

#model  prediction
  lst = []
  res = holis.process(imgRGB)

  for i in res.pose_landmarks.landmark:
    lst.append(i.x - res.pose_landmarks.landmark[0].x)
    lst.append(i.y - res.pose_landmarks.landmark[0].y)

  lst = np.array(lst).reshape(1,-1)

  p = model.predict(lst)
  pred = label[np.argmax(p)]
  print(pred)
  if current_pose == pred:
    change = True
    score += 1
  # print(pred)
  #/////////
  
  #add images
  window.blit(imgTpose, (0,0) )

  #update display
  pygame.display.update()

  #set fps
  clock.tick(fps)

