import cv2
import numpy as np
import datetime 
camera = cv2.VideoCapture(0)
contador = 1 
car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_alt.xml")

def recognitionObject():
  height, width, c = frame.shape
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  objetos = car_cascade.detectMultiScale(gray, 1.2, 5)
  print(objetos)
  for (x,y,w,h) in objetos:
    imgImportant = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    imgImportant = gray[y:y+h, x:x+w]
    cv2.imshow("Interesse", imgImportant)
    cv2.imwrite("simbolo_detect/" + str("Deteccao"+str(contador)) +".jpg", frame)
  cv2.imshow("Camera", frame)

def recognitionFrontalFace():
  frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  detect = cascade.detectMultiScale(frameGray, 1.1, 5)
  for (x,y,w,h) in detect:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    clipImage()
  cv2.imshow("Camera", frame)

def closeFileRed():
  lower_red = np.array([161, 155, 84], np.uint8)
  upper_red = np.array([179, 255, 255], np.uint8)
  red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
  result = cv2.bitwise_and(frame, frame, mask=red_mask)
  frame_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

  _, thresh = cv2.threshold(frame_gray, 3, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(
      thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  
  for contour in contours:
      (x, y, w, h) = cv2.boundingRect(contour)
      area = cv2.contourArea(contour)
      if area > 1000:
          cv2.putText(frame, "Red detected", (10, 80),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
          cv2.destroyAllWindows()
          camera.release()
      cv2.imshow("Camera", frame)

def clipImage():
  frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  detect = cascade.detectMultiScale(frameGray, 1.1, 5)
  for (x, y, w, h) in detect:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    imgImportant = frameGray[y:y+h, x:x+w]
    cv2.imshow("Interesse", imgImportant)

def binarization():
  binarizationObject = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  ImagemGaussianBlur = cv2.GaussianBlur(binarizationObject, (7, 7), 0) 
  _, ImagemThrehold = cv2.threshold(ImagemGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV)
  ImagemAdaptive = cv2.adaptiveThreshold(
    ImagemGaussianBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 10)  
  ImagemUnited = np.vstack(
    [np.hstack([ImagemThrehold, ImagemAdaptive])]) 
  cv2.imshow("Imagem Binária", ImagemUnited)
  return 

def changeColor():
  lower_red = np.array([36, 42, 91])
  upper_red = np.array([255, 255, 255])
  mask = cv2.inRange(hsv_frame, lower_red, upper_red)
  res = cv2.bitwise_not(frame, frame, mask = mask)
  rest = cv2.bitwise_and(frame, frame, mask = mask)
  res[mask>0] = (255, 0, 0)
  cv2.imshow('Resultado', res)

def morphology():
  binarizationObject = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  ImagemGaussianBlur = cv2.GaussianBlur(binarizationObject, (7, 7), 0) 
  _, ImagemThrehold = cv2.threshold(ImagemGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV)
  ImagemAdaptive = cv2.adaptiveThreshold(
    ImagemGaussianBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 10)

  kernel = np.ones((5, 5), np.uint8)
  opening = cv2.morphologyEx(ImagemAdaptive, cv2.MORPH_OPEN, kernel)
  closing = cv2.morphologyEx(ImagemAdaptive, cv2.MORPH_CLOSE, kernel)
  cv2.imshow("Opening", opening)
  cv2.imshow("Closing", closing)

def redimensionamento():
  height, width = frame.shape[:2]
  res = cv2.resize(frame,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
  cv2.imshow("Rezise:", res)

def processing():
  grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converte a imagem original para tons de cinza a fim de eliminar os ruídos da imagem 
  hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converte a imagem original para o formato de cores HSV
  labImage = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB) #Converte a imagem original para o formato de cores Lab
  equalizedImage = cv2.equalizeHist(grayImage) #Aumenta o contraste da imagem  - Equalizando o histograma para melhorar os objetos seu recoquecimento

  cv2.imshow("Image with shades of gray", grayImage)
  cv2.imshow("Equalized Image", equalizedImage)
  cv2.imshow("Image with HSV", hsvImage)
  cv2.imshow("Image with Lab", labImage)
  
  imageGaussianBlur = cv2.GaussianBlur(grayImage, (7, 7), 0) #Embaça a imagem com o objetivo de eliminar ruídos que possam prejudicá-la
  _, imageThrehold = cv2.threshold(imageGaussianBlur, 120, 255, cv2.THRESH_BINARY_INV) #Aplica a técnica de binarização threshold
  imageAdaptive = cv2.adaptiveThreshold(
    imageGaussianBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 10) # Ignora a vizinhânça de 50 (Quantidade de pixel a ser ignorado) - Bloco de vizinhância que ele irá analisar - 50. Constante (valor que ele irá reduzir do pixels para dizer se irão ou não fazer parte da saída do algoritmo) 
  
  ##################### Detecção de bordas #####################
  imageSobelEixoX = cv2.Sobel(imageGaussianBlur, cv2.CV_64F, 1, 0) #Converte a figura a nível de execução no eixo x
  imageSobelEixoY = cv2.Sobel(imageGaussianBlur, cv2.CV_64F, 0, 1) #Converte a figura a nível de execução no eixo y
  imageSobelEixoX = np.uint8(np.absolute(imageSobelEixoX)) #Reconverte para o formato padrão de 8bits que antes tinha sido aumentado para 64 bits durante o processamento
  imageSobelEixoY = np.uint8(np.absolute(imageSobelEixoY))
  imageSobel = cv2.bitwise_or(imageSobelEixoX, imageSobelEixoY)

  imageUnitedSobel = np.vstack(
      [np.hstack([grayImage, imageSobelEixoX]), np.hstack([imageSobelEixoY, imageSobel])]) #Coloca na linha horizontal as imagens
  cv2.imshow("Sobel", imageUnitedSobel)

while True:
  ret, frame = camera.read()
  frame = cv2.flip(frame, 1)
  hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  #recognitionObject()
  #recognitionFrontalFace()
  #redimensionamento()
  #closeFileRed()
  #binarization()
  #processing()
  #changeColor()
  morphology()

  if ret: 
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
    dt = str(datetime.datetime.now()) #detectar data hora
    frame = cv2.putText(frame, dt, (10, 100), font, 1, (155, 155, 155), 1, cv2.LINE_8) 
    contador += 1
    cv2.imshow('Camera', frame) 
    key = cv2.waitKey(1) 
    if key == 27: 
      break

cv2.destroyAllWindows()
camera.release()
