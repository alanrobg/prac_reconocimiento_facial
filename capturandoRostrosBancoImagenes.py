import cv2
import os

imagesPath = 'C:/Users/ARG/Documents/proyectos/reconocimiento_facial/imagenes'
imagesPathList = os.listdir(imagesPath)
print('imagesPathList=',imagesPathList)

if not os.path.exists('Rostros_encontrados'):
    print('Carpeta creada: Rostros encontrados')
    os.makedirs('Rostros_encontrados')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

count = 0

for imageName in imagesPathList:
    #print('imageName=',imageName)
    image = cv2.imread(imagesPath+'/'+imageName)
    imageAux=image.copy()
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(38,31,184),2)
    cv2.rectangle(image,(10,5),(450,25),(255,255,355),-1)
    cv2.putText(image,'Presione s, para almacenar',(10,20),2,0.5,(128,0,255),1,cv2.LINE_AA)
    cv2.imshow('image',image)
    k = cv2.waitKey(0)
    if k == ord("s"):
        for(x,y,w,h) in faces:
            rostro = imageAux[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
            #cv2.imshow('rostro',rostro)
            #cv2.waitKey(0)
            cv2.imwrite('Rostros_encontrados/rostro_{}.jpg'.format(count),rostro)
            count = count+1
    elif k==27:
        break

cv2.destroyAllWindows()