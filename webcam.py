import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cnn_model = keras.models.load_model("cnn_model")
while True:
    success, img = webcam.read()
    if success:
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cats = cat_cascade.detectMultiScale(gray, 1.25, minNeighbors = 2)
        
        for (x,y,w,h) in cats:
            roi_rgb = img[y:y+h, x:x+w]
            new_array = cv2.resize(roi_rgb,(160, 160))
            pic_matrix = np.array(new_array).astype('float32')
            pic_matrix /= 25.0
            pic_matrix = pic_matrix.reshape(1, 160, 160, 3)
            cat_breed = np.argmax(cnn_model.predict(pic_matrix), axis =1)
            label = ['Orange Tabby', 'Siamese', 'Bombay']
            
            color =(0, 0, 255)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, label[int(cat_breed)-1], (x,y), font,1, color, 2, cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
webcam.release()
cv2.destroyAllWindows()