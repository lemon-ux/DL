import sys
import os.path
if __name__ == "__main__":
    BASE_PATH="C:/face_recognition/jm"
    
    SEPARATOR=";"
 
    fh = open("C:/face_recognition/jm/at.text",'w')
 
    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                print ("%s%s%d" % (abs_path, SEPARATOR, label))
                fh.write(abs_path)
                fh.write(SEPARATOR)
                fh.write(str(label))
                fh.write("\n")      
            label = label + 1
    fh.close()
