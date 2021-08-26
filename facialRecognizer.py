import cv2
import imutils
import face_recognition
import os

def faceDetect(img):
    try:
        loadAlgoritmo = cv2.CascadeClassifier(os.path.abspath('C:/Users/Ruty Ribeiro/Documents/MeusProjetos/TCC-Faculdade/backend/Haar/haarcascade_frontalface_default.xml'))

        imagem = imutils.url_to_image(img)
        # print(imagem)
        # imagem=cv2.imread(img)
        imagemcinza=cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        faces = loadAlgoritmo.detectMultiScale(imagemcinza,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30))
 
        return (len(faces))

    except Exception as error:
         return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

def faceRecognition(imgUser, imgBD):

    try:
        hasFace = faceDetect(imgUser)

        if type(hasFace) == dict:
            return hasFace
        elif hasFace != 1:
            raise Exception('Foto invalida! Tente novamente ou selecione outra foto.')
        else:
            # imageUser= face_recognition.load_image_file(imgUser)
            imageUser= imutils.url_to_image(imgUser)
            imageUser_encoding = face_recognition.face_encodings(imageUser)[0]

            # imageBD = face_recognition.load_image_file(imgBD)
            imageBD= imutils.url_to_image(imgBD)
            imageBD_encoding = face_recognition.face_encodings(imageBD)[0]
                
            # Compara as faces
            results = face_recognition.compare_faces([imageUser_encoding], imageBD_encoding, 0.5)
            
            if not results[0]:
                raise Exception ('Usuário não reconhecido! Tente novamente ou cadastre-se.')
            else:
                return True
    
    except Exception as error:
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'}) 
                
# print(faceDetect('https://firebasestorage.googleapis.com/v0/b/tcc-faculdade-bfbb8.appspot.com/o/userPhotos%2Fmai.jpg?alt=media&token=eb632775-2175-4072-b2c5-d4747a873ea2'))
# print(faceRecognition('https://firebasestorage.googleapis.com/v0/b/tcc-faculdade-bfbb8.appspot.com/o/retrievePhotos%2Fmarllon.jpg?alt=media&token=97645bc7-fead-4ef8-be4b-949948e88c16',
# 'https://firebasestorage.googleapis.com/v0/b/tcc-faculdade-bfbb8.appspot.com/o/userPhotos%2FUser.1.0.jpg?alt=media&token=d7b66e5e-9c5e-4d6e-9afe-a823d3f1f0ba'))
