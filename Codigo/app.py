import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import cv2
import time
import numpy as np
import copy
import statistics
from tkinter import filedialog
import sys, os


class UI(QMainWindow):

    img = None
    final_image = None   #Variables globales para conservar ultimos resultados
    krn = None
    sz = None    

    def __init__(self):
        super().__init__()
        path = self.resource_path("gui_app.ui")
        uic.loadUi(path,self)
    

        self.boton_imagen.clicked.connect(self.fn_seleccionar)  #Botones asignados a los filtros, ruidos, guardado y seleccionado de imagenes.
        self.boton_guardar.clicked.connect(self.fn_guardar)

        self.boton_kernel.clicked.connect(self.generate_kernel)
        self.boton_max.clicked.connect(self.filtro_max)
        self.boton_min.clicked.connect(self.filtro_min)
        self.boton_medio.clicked.connect(self.filtro_puntomedio)
        self.boton_alfa.clicked.connect(self.filter_corteAlfa)
        self.boton_uni.clicked.connect(self.ruido_uniforme)
        self.boton_exp.clicked.connect(self.ruido_exponencial)

    
    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def fn_seleccionar(self):#Seleccion de la imagen
        
        path_image = filedialog.askopenfilename()
        global img
        img = cv2.imread(path_image)
        self.pixmap = QPixmap(path_image).scaled(401,241, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.muestra_imagen.setPixmap(self.pixmap)
        
    
    def fn_guardar(self):#Guardado del ultimo resultado
        global final_image

        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
        
        try:
            cv2.imwrite(f"image {tiempo}.jpg", final_image)
        except NameError:
            self.show_pop("No se ha seleccionado una imagen")
            return


    def generate_kernel(self):#Genera kernel
        global krn
        global sz

        try:
            sz = size = int(self.valor_mn.toPlainText())
        except NameError:
            self.show_pop("Tamaño del kernel no definido")
            return
        except ValueError:
            self.show_pop("Tamaño del kernel no fue definido correctamente")
            return

        
        if sz <= 1:
            self.show_pop("Tamaño del kernel no se puede definir menor a 2")
            return

        mtx = [[1 for x in range(size)] for y in range(size)] 
        new_mtx = []


        if(size%2 == 0):
            
            new_mtx = [[0 for x in range(size+1)] for y in range(size+1)]
            for i in range(size):
                for j in range(size):
                    new_mtx[i][j] = new_mtx[i][j] + mtx[i][j]
            
            self.et_kernel.setText(f"{size}x{size}")
            mn = size*size
            self.et_kernel_3.setText(f"{mn}")
            self.et_kernel_4.setText(f"Ingrese valor d menor a {mn}")
            krn = copy.deepcopy(new_mtx)

        else:
            self.et_kernel.setText(f"{size}x{size}")
            mn = size*size
            self.et_kernel_3.setText(f"{mn}")
            self.et_kernel_4.setText(f"Ingrese valor d menor a {mn}")
            krn = copy.deepcopy(mtx)

    def filtro_max(self):#Aplica el filtro max


        global krn
        global final_image
        global img
        global sz

        try:
            image = img
            kernel = krn
            tam = sz
        except NameError:
            self.show_pop("Imagen o kernel no definido")
            return
            

        arr_image = image.tolist()
        aux_arr_image = copy.deepcopy(arr_image)# Se copia la imagen
        aux_tam = 0
            
        if tam%2 == 0:
            aux_tam = int(tam/2)
        else:
            aux_tam = int((tam-1)/2)
            
        for i in range(len(arr_image)):#Expandir la matriz de la imagen del lado izquierdo y derecho
            for j in range(aux_tam):
                arr_image[i] = [arr_image[i][0]] + arr_image[i] + [arr_image[i][len(arr_image[i])-1]]


                #Expandir la matriz de la imagen del lado superior e inferior
        for i in range(aux_tam):
            arr_image = [arr_image[0]] + arr_image + [arr_image[len(arr_image)-1]]


        if(len(image.shape)<3):
            new_matrix = [[0 for x in range(len(aux_arr_image[0]))] for y in range(len(aux_arr_image))] 
                
                

            for i in range(len(aux_arr_image)):#Precaucion: Tamaño = original de la lista
                for j in range(len(aux_arr_image[0])):#Precaucion: Tamaño = original de la lista
                    list_res = list()
                    for k in range(len(kernel)):# Se recorre el kernel
                        for m in range(len(kernel[0])):
                            list_res.append(kernel[k][m]*arr_image[i+k][j+m])
                    new_matrix[i][j] = max(list_res)
            

            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Max-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

        elif len(image.shape)==3:
            new_matrix = [[[0 for x in range(len(aux_arr_image[0][0]))] for y in range(len(aux_arr_image[0]))] for z in range(len(aux_arr_image))]

            for dim in range(image.shape[2]):
                for i in range(len(aux_arr_image)):
                    for j in range(len(aux_arr_image[0])):
                        list_res = list()
                        for m in range(len(kernel)):
                            for n in range(len(kernel[0])):
                                list_res.append(kernel[m][n]*arr_image[i+m][j+n][dim])
                        
                        new_matrix[i][j][dim] =  max(list_res)
            

            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Max-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)
    
    def filtro_min(self):#Aplica el filtro min

        global krn
        global final_image
        global img
        global sz

        try:
            image = img
            kernel = krn
            tam = sz
        except NameError:
            self.show_pop("Imagen o kernel no definido")
            return



        arr_image = image.tolist()
        aux_arr_image = copy.deepcopy(arr_image)
        aux_tam = 0
        
        if tam%2 == 0:
            aux_tam = int(tam/2)
        else:
            aux_tam = int((tam-1)/2)
        
        for i in range(len(arr_image)):
            for j in range(aux_tam):
                arr_image[i] = [arr_image[i][0]] + arr_image[i] + [arr_image[i][len(arr_image[i])-1]]

            

            #Expandir la matriz de la imagen del lado superior e inferior
        for i in range(aux_tam):
            arr_image = [arr_image[0]] + arr_image + [arr_image[len(arr_image)-1]]


        if(len(image.shape)<3):
            new_matrix = [[0 for x in range(len(aux_arr_image[0]))] for y in range(len(aux_arr_image))] 
            
            

            for i in range(len(aux_arr_image)):#Precaucion: Tamaño = original de la lista
                for j in range(len(aux_arr_image[0])):#Precaucion: Tamaño = original de la lista
                    list_res = list()
                    for k in range(len(kernel)):
                        for m in range(len(kernel[0])):
                            list_res.append(kernel[k][m]*arr_image[i+k][j+m])
                    new_matrix[i][j] = min(list_res)

            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Min-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

        elif len(image.shape)==3:
            new_matrix = [[[0 for x in range(len(aux_arr_image[0][0]))] for y in range(len(aux_arr_image[0]))] for z in range(len(aux_arr_image))]

            for dim in range(image.shape[2]):
                for i in range(len(aux_arr_image)):
                    for j in range(len(aux_arr_image[0])):
                        list_res = list()
                        for m in range(len(kernel)):
                            for n in range(len(kernel[0])):
                                list_res.append(kernel[m][n]*arr_image[i+m][j+n][dim])
                        new_matrix[i][j][dim] =  min(list_res)
            
            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Min-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

    def filtro_puntomedio(self):#Aplica el filtro de punto medio
        global krn
        global final_image
        global img
        global sz

        try:
            image = img
            kernel = krn
            tam = sz
        except NameError:
            self.show_pop("Imagen o kernel no definido")
            return



        arr_image = image.tolist()
        aux_arr_image = copy.deepcopy(arr_image)
        aux_tam = 0
        
        if tam%2 == 0:
            aux_tam = int(tam/2)
        else:
            aux_tam = int((tam-1)/2)
        
        for i in range(len(arr_image)):
            for j in range(aux_tam):
                arr_image[i] = [arr_image[i][0]] + arr_image[i] + [arr_image[i][len(arr_image[i])-1]]

            #print("\n",arr_image,"\n")

            #Expandir la matriz de la imagen del lado superior e inferior
        for i in range(aux_tam):
            arr_image = [arr_image[0]] + arr_image + [arr_image[len(arr_image)-1]]


        if(len(image.shape)<3):
            new_matrix = [[0 for x in range(len(aux_arr_image[0]))] for y in range(len(aux_arr_image))] 
            
            

            for i in range(len(aux_arr_image)):#Precaucion: Tamaño = original de la lista
                for j in range(len(aux_arr_image[0])):#Precaucion: Tamaño = original de la lista
                    list_res = list()
                    for k in range(len(kernel)):
                        for m in range(len(kernel[0])):
                            list_res.append(kernel[k][m]*arr_image[i+k][j+m])
                    new_matrix[i][j] = (max(list_res) + min(list_res))/2

            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Pun-Med-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

        elif len(image.shape)==3:
            new_matrix = [[[0 for x in range(len(aux_arr_image[0][0]))] for y in range(len(aux_arr_image[0]))] for z in range(len(aux_arr_image))]

            for dim in range(image.shape[2]):
                for i in range(len(aux_arr_image)):
                    for j in range(len(aux_arr_image[0])):
                        list_res = list()
                        for m in range(len(kernel)):
                            for n in range(len(kernel[0])):
                                list_res.append(kernel[m][n]*arr_image[i+m][j+n][dim])
                        new_matrix[i][j][dim] =  (max(list_res) + min(list_res))/2
            
            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Pun-Med-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)


    def filter_corteAlfa(self):#Aplica el filtro medio de corte alfa
        global krn
        global final_image
        global img
        global sz

        try:
            image = img
            kernel = krn
            tam = sz
        except NameError:
            self.show_pop("Imagen o kernel no definido")
            return
        
        try:
            d = int(self.valor_d.toPlainText())
        except NameError:
            self.show_pop("d no esta definido")
            return
        except ValueError:
            self.show_pop("d no esta definido correctamente")
            return
        
        if (d < 0 or d >= (tam*tam)):
            self.show_pop(f"d es un numero negativo o es mayor o igual a {tam*tam}")
            return


        arr_image = image.tolist()
        aux_arr_image = copy.deepcopy(arr_image)
        aux_tam = 0
        
        if tam%2 == 0:
            aux_tam = int(tam/2)
        else:
            aux_tam = int((tam-1)/2)
        
        for i in range(len(arr_image)):
            for j in range(aux_tam):
                arr_image[i] = [arr_image[i][0]] + arr_image[i] + [arr_image[i][len(arr_image[i])-1]]


            #Expandir la matriz de la imagen del lado superior e inferior
        for i in range(aux_tam):
            arr_image = [arr_image[0]] + arr_image + [arr_image[len(arr_image)-1]]


        mn = tam * tam
        
        value = mn-d


        if(len(image.shape)<3):
            new_matrix = [[0 for x in range(len(aux_arr_image[0]))] for y in range(len(aux_arr_image))] 
            
            

            for i in range(len(aux_arr_image)):#Precaucion: Tamaño = original de la lista
                for j in range(len(aux_arr_image[0])):#Precaucion: Tamaño = original de la lista
                    list_res = list()
                    for k in range(len(kernel)):
                        for m in range(len(kernel[0])):
                            list_res.append(kernel[k][m]*arr_image[i+k][j+m])
                    if(value == 1):
                        new_matrix[i][j] = statistics.median(list_res)
                    else:
                        Sum = sum(list_res)/value
                        if(Sum >= 256):
                            new_matrix[i][j] = 255
                        else:
                            new_matrix[i][j] = Sum


            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")
            cv2.imshow(f'Imagen-filtro-Medio-alfa-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

        elif len(image.shape)==3:
            new_matrix = [[[0 for x in range(len(aux_arr_image[0][0]))] for y in range(len(aux_arr_image[0]))] for z in range(len(aux_arr_image))]

            for dim in range(image.shape[2]):
                for i in range(len(aux_arr_image)):
                    for j in range(len(aux_arr_image[0])):
                        list_res = list()
                        for m in range(len(kernel)):
                            for n in range(len(kernel[0])):
                                list_res.append(kernel[m][n]*arr_image[i+m][j+n][dim])
                        if(value == 1):
                            new_matrix[i][j][dim] =  statistics.median(list_res)
                        else:
                            Sum = sum(list_res)/value
                            if(Sum >= 256):
                                new_matrix[i][j][dim] = 255
                            else:
                                new_matrix[i][j][dim] = Sum
            
            final_image = im_filter = np.array(new_matrix)

            tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

            cv2.imshow(f'Imagen-filtro-Medio-alfa-{tiempo}', im_filter.astype(np.uint8))
            cv2.waitKey(0)

    def show_pop(self, text):#Muestra las notificaciones de error
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        x = msg.exec_()

    def rgb_to_grayscale(self,pic):#Realiza la conversion a escala de grises
        if(len(pic.shape) == 3):

            r = pic[:,:,0]
            g = pic[:,:,1]
            b = pic[:,:,2]

            gray = (0.2989 * r) + (0.5870 * g) + (0.1140 * b)

            return gray

        elif(len(img.shape) < 3):
            return img

    def ruido_uniforme(self):#Aplica el ruido uniforme aleatorio
        global final_image
        global img

        try:
            a = int(self.valor_a_uni.toPlainText())
            b = int(self.valor_b_uni.toPlainText())
        except NameError:
            self.show_pop("a y/o b no estan definidas")
            return
        except ValueError:
            self.show_pop("a y/o b no estan definidas correctamente")
            return
        

        if ((a<0 or a>255) or  (b<0 or b>255)):
            self.show_pop("a y/o no estan definidos entre 0 y 255")
            return
        elif(a>b):
            self.show_pop("a es mayor que b")
            return

        try:
            image = img
        except NameError:
            self.show_pop("No se ha seleccionado una imagen")
            return        


        gray_image = self.rgb_to_grayscale(image)

        arr_image = gray_image.tolist()

        new_matrix = [[0 for x in range(len(arr_image[0]))] for y in range(len(arr_image))]

        for i in range(len(arr_image)):
            for j in range(len(arr_image[0])):
                ruido = np.random.uniform(a,b)
                if(arr_image[i][j]>= a and arr_image[i][j]<= b):
                    new_matrix[i][j] = arr_image[i][j] + 0
                if((ruido + arr_image[i][j]) >= 256):
                    new_matrix[i][j] = 255
                else:
                    new_matrix[i][j] = arr_image[i][j] + ruido
        
        final_image = im_ruido = np.array(new_matrix)

        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

        cv2.imshow(f'Imagen-Ruido-Uni-{tiempo}', im_ruido.astype(np.uint8))
        cv2.waitKey(0)



    def ruido_exponencial(self):#Aplica el ruido exponencial aleatorio
        global final_image
        global img

        try:
            a = int(self.valor_a_exp.toPlainText())
        except NameError:
            self.show_pop("a no esta definido")
            return
        except ValueError:
            self.show_pop("a no esta definido correctamente")
            return

        if (a<0 or a>255):
            self.show_pop("a no esta entre 0 y 255")
            return

        
        try:
            image = img
        except NameError:
            self.show_pop("No se ha seleccionado una imagen")
            return



        gray_image = self.rgb_to_grayscale(image)

        arr_image = gray_image.tolist()

        new_matrix = [[0 for x in range(len(arr_image[0]))] for y in range(len(arr_image))]

        for i in range(len(arr_image)):
            for j in range(len(arr_image[0])):
                ruido = np.random.exponential(a)
                if((ruido + arr_image[i][j]) >= 256):
                    new_matrix[i][j] = 255
                else:
                    new_matrix[i][j] = arr_image[i][j] + ruido
        
        final_image = im_ruido = np.array(new_matrix)

        tiempo = time.strftime("%d-%m-%Y-%H-%M-%S")

        cv2.imshow(f'Imagen-Ruido-Exp-{tiempo}', im_ruido.astype(np.uint8))
        cv2.waitKey(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())