from cv2 import cv2
import os
 
def generate(dirname):
     
    #加载opencv自带的人脸分类器
    face_cascade = cv2.CascadeClassifier("D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml")
    if(not os.path.isdir(dirname)):
        os.makedirs(dirname)
  
    camera = cv2.VideoCapture(0)
    count = 0
    while (True):
        # 按帧读取视频，ret为布尔值，读帧正确返回true，frame为每一帧的图像
        ret, frame = camera.read()
        # 生成灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            #识别到物体后进行剪裁
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            # 保存
            cv2.imwrite(dirname + '/%s.pgm' % str(count), f)
            print(count)
            count += 1

        # 显示图像，camera为显示图像的窗口的名字，frame为要显示的图像
        cv2.imshow("camera", frame)
        # 等待键盘输入，0表示无限等待，按下q则返回按键的ASCII码退出
        if cv2.waitKey(100) & 0xff == ord("q"):
            break
        elif count > 20:
            break
 
    # 释放，销毁所有窗口
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate("C:/face_recognition/jm")