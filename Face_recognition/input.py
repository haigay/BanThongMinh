from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

#Khởi tạo thông số camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(320, 240))

#Load file cascade để phát hiện mặt
face_cascade = cv2.CascadeClassifier('/home/admin/Desktop/Face_recognition/haarcascade_frontalface_default.xml')

#Thêm id người mới
face_id = input("\nUser id :") 
print ("\n[INFO] Initializing face capture. Look the camera and wait ...")
count = 0

# Bắt đầu chụp hình
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image = cv2.flip(image,-1)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Phát hiện khuôn mặt trong hình
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (100, 100), flags = cv2.CASCADE_SCALE_IMAGE)
    
    #Vẽ khung
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    #Save hình
    if len(faces):
        count = count + 1
        img_item = "dataSet/User."+ face_id + '.' + str(count) + ".jpg"
        cv2.imwrite(img_item,roi_gray)
        print("Số lượng ảnh đã chụp:",count)

    cv2.imshow("Frame", image)
    if cv2.waitKey(1) & 0xff == ord("q"):
        exit()
    if count == 500:
        exit()
    
    rawCapture.truncate(0)