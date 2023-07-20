from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import socket

# Thông tin kết nối socket
host = '192.168.1.157'
port = 8000

# Tạo socket và kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Khởi tạo camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(320, 240))
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load file train
recognizer.read('/home/admin/Desktop/Face_recognition/trainer/trainer.yml')

# Load file casscade
face_cascade = cv2.CascadeClassifier('/home/admin/Desktop/Face_recognition/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['Hai', 'Huy', 'Hao', 'unknow']

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image,-1)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # detect mặt bằng file casscade
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)
 
    # Vẽ khung
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Kiểm tra
        if (confidence < 100):
            message = id
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            print(id,confidence)
            # Gửi message đến server
            client_socket.sendall(message.encode())
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            print(id,confidence)
 
        cv2.putText(image, str(id), (x+5,y-5), font, 1, (255,255,255), 2)

    cv2.imshow("Frame", image)
    if cv2.waitKey(1) & 0xff == ord("q"):
        message = 'q'
        # Gửi q về server
        client_socket.sendall(message.encode())
        exit()

    rawCapture.truncate(0)