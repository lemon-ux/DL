from cv2 import cv2
import os
import sys
import numpy as np

def read_images(path, sz = None):
    # 第c张图
    c = 0
    X, y = [], []

    for dirname, dirnames, filenames in os.walk(path):
        subject_path = dirname
        for filename in os.listdir(subject_path):
            try:
                if not filename.endswith('.pgm'):
                    continue
                filepath = os.path.join(subject_path, filename)

                #读取图片后已多维数组的形式保存图片信息，前两维表示图片的像素坐标，最后一维表示图片的通道索引
                im = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

                if sz is not None:
                    im = cv2.resize(im,(200,200))
                X.append(np.asarray(im, dtype=np.uint8))
                y.append(c)
            except:
                print("Unexpected error:",sys.exc_info()[0])
            c = c + 1
    return [X, y]

def face_rec(img_path):
    names = ['rabbit']
    [X,y] = read_images(img_path)
    y = np.asarray(y, dtype=np.int32)

    # 特征脸人脸识别算法
    model = cv2.face.EigenFaceRecognizer_create()
    # 传入特征值和特征标签进行训练
    model.train(np.asarray(X), np.asarray(y))
    
    #参数为0，表示打开默认的摄像机
    camera = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(r"D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    while (True):
        read, img = camera.read()
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi = gray[x: x+w, y: y+h]
            try:
                # 读入用于识别的人脸
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                # 进行识别，返回标签和置信度
                params = model.predict(roi)
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))

                # 增加文本内容
                cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

            except:
                continue
        cv2.imshow("camera", img)
        if cv2.waitKey(1000 // 12) & 0xff == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_rec(r'C:/face_recognition/jm')