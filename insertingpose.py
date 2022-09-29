import mediapipe as mp 
import numpy as np 
import cv2 

def inFrame(lst):
	if lst[28].visibility > 0.6 and lst[27].visibility > 0.6 and lst[15].visibility>0.6 and lst[16].visibility>0.6:
		return True 
	return False
 
cap = cv2.VideoCapture(0)

name = input("Enter the name of the pose : ")

holistic = mp.solutions.pose
holis = holistic.Pose()
drawing = mp.solutions.drawing_utils

X = []
data_size = 0

while True:
	lst = []

	_, frm = cap.read()

	frm = cv2.flip(frm, 1)

	res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

	if res.pose_landmarks and inFrame(res.pose_landmarks.landmark):
		for i in res.pose_landmarks.landmark:
			lst.append(i.x - res.pose_landmarks.landmark[0].x)
			lst.append(i.y - res.pose_landmarks.landmark[0].y)

		X.append(lst)
		data_size = data_size+1

	else: 
		cv2.putText(frm, "Make Sure Full body visible", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

	drawing.draw_landmarks(frm, res.pose_landmarks, holistic.POSE_CONNECTIONS)

	cv2.putText(frm, str(data_size), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

	cv2.imshow("window", frm)

	if cv2.waitKey(1) == 27 or data_size>80:
		cv2.destroyAllWindows()
		cap.release()
		break


np.save(f"{name}.npy", np.array(X))
print(np.array(X).shape)



import os  
import numpy as np 
import cv2 
from tensorflow.keras.utils import to_categorical

from keras.layers import Input, Dense 
from keras.models import Model
 
is_init = False
size = -1

label = []
dictionary = {}
c = 0

for i in os.listdir():
	if i.split(".")[-1] == "npy" and not(i.split(".")[0] == "labels"):  
		if not(is_init):
			is_init = True 
			X = np.load(i)
			size = X.shape[0]
			y = np.array([i.split('.')[0]]*size).reshape(-1,1)
		else:
			X = np.concatenate((X, np.load(i)))
			y = np.concatenate((y, np.array([i.split('.')[0]]*size).reshape(-1,1)))

		label.append(i.split('.')[0])
		dictionary[i.split('.')[0]] = c  
		c = c+1


for i in range(y.shape[0]):
	y[i, 0] = dictionary[y[i, 0]]
y = np.array(y, dtype="int32")


y = to_categorical(y)

X_new = X.copy()
y_new = y.copy()
counter = 0 

cnt = np.arange(X.shape[0])
np.random.shuffle(cnt)

for i in cnt: 
	X_new[counter] = X[i]
	y_new[counter] = y[i]
	counter = counter + 1


ip = Input(shape=(X.shape[1]))

m = Dense(128, activation="tanh")(ip)
m = Dense(64, activation="tanh")(m)

op = Dense(y.shape[1], activation="softmax")(m) 

model = Model(inputs=ip, outputs=op)

model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc'])

model.fit(X_new, y_new, epochs=80)


model.save("model.h5")
np.save("labels.npy", np.array(label))
