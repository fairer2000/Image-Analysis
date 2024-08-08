# Image Analysis - Analisis de Imágenes

Este proyecto es una herramienta de análisis de imágenes que permite aplicar y eliminar el ruido de imágenes utilizando técnicas avanzadas de visión por computadora.

## Requisitos previos
Asegurate de tener instalado

- OpenCV
- Numpy
- Tkinter
- PyQT5

Para hacer uso del programa, basta con ejecutar el siguiente comando en cmd.

```cmd
python .\app.py
```

## Uso del programa.
Al ejecutar el comando previamente mostrado, se deberá desplejar el menu del programa.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8cb5d2ce-94bc-4d17-a48a-e712f8303f23" alt="menu" />
</p>

Dentro tendremos las opciones de aplicar determinados filtros y ruidos estadisticos, el tamaño del kernel y la selección de las variables que se requieren en algunos filtros y ruidos. También se permite la selección de la imagen a modificar, así como el guardado de la imagen modificada.

## Funciones del programa

### Aplicación del kernel

Para aplicar el kernel, se debe de escribir el valor en el cuadro correspondiente. Cabe aclarar que se debe de pensar el valor a asignar, ya que conforme más grande sea el kernel mayor será el tiempo que tomará en obtenerse un resultado en la aplicación de los filtros.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a469c96b-de5f-42b6-956b-8b4cc880ff67" alt="Select Kernel" />
</p>

Para los siguientes ejemplos, se usará un kernel de 5x5.

### Seleccionar imagen

Para el ejemplo, primero debemos seleccionar una imagen. Damos click en el botón "Seleccionar imagen". Se desplegará una ventan para la selección de la imagen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9824a9a6-e2f3-4bb3-b32b-cb9d7a8c3eed" alt="Image selection window" />
</p>

Se selecciona la imagen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bb8f8c0e-d95e-4d53-9d37-76adc7ebdf1f" alt="Select image" />
</p>

Se mostrará la imagen seleccionada en el menu.

<p align="center">
  <img src="https://github.com/user-attachments/assets/904dd4a0-24df-4287-80b6-4484effaeb82" alt="Selected image in menu" />
</p>

Al tener la imagen seleccionada y el kernel aplicado, se puede proceder a aplicar los filtros.

### Filtro Máximo

Damos click al botón "Filtro max" para aplicar el filtro estadístico sobre la imagen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/92816f3f-c8d4-4589-8443-f81b2626490a" alt="Max filter applied" />
</p>



### Filtro Mínimo

Damos click al botón "Filtro min" para aplicar el filtro estadístico sobre la imagen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2455ed08-c331-4108-be3f-0a94e1fee723" alt="Min filter applied" />
</p>



### Filtro de Punto Medio.

Damos click al botón "Filtro punto medio" para aplicar el filtro estadístico sobre la imagen.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec4acc4e-ed85-4f96-812a-32aff4aacd77" alt="Median filter" />
</p>


### Filtro Medio de Corte Alfa

En este filtro debemos de declarar un valor para d, mientras el valor no sea mayor a la dimensión del kernel (mxn), declaramos un valor de 10.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b6474b62-c430-4e0f-82a0-8a9df9cdd97c" alt="Select d" />
</p>

Ahora podemos aplicar el filtro haciendo click en el botón "Filtro Medio de Corte Alfa".

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b5da02b-eca3-46a0-9806-cff616bbbfa4" alt="Alpha-Trimmed Mean Filter" />
</p>


### Ruido Uniforme

Para aplicar el Ruido Uniforme debemos de declarar las variables a y b. Las variables deben de estar en un rango de 0 a 255, y b debe ser mayor que la variable a.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a7b6eb66-0ca3-4f2f-ba3a-afac786479b8" alt="Select Uniform Noise" />
</p>

Con las variables declaradas, aplicamos el ruido haciendo click en el botón "Ruido uniforme".

<p align="center">
  <img src="https://github.com/user-attachments/assets/a06bf225-070b-4819-b6f5-420ea30dd30e" alt="Uniform Noise" />
</p>


### Ruido Exponencial

Para aplicar el Ruido Exponencial debemos de declarar la variables a. La variable deben de estar en un rango de 0 a 255.
<p align="center">
  <img src="https://github.com/user-attachments/assets/b80daf91-b54b-457d-9fe5-1f1e5051d23f" alt="Select Exponential Noise" />
</p>

Ahora podemos aplicar el ruido haciendo click en el botón "Ruido exponencial".

<p align="center">
  <img src="https://github.com/user-attachments/assets/9fa2dcdf-e1f0-4607-8a35-86f0a61e54e4" alt="Exponential Noise" />
</p>


### Guardar imagen

Si queremos guardar el resultado, debemos hacer click en el botón "Guardar imagen". Se desplegará una ventana para el guardado de la imagen, en donde se podrá cambiar el nombre de la imagen y la extensión si es necesario.

<p align="center">
  <img src="https://github.com/user-attachments/assets/315f0e77-50ba-4b85-b879-36c6e663f2b2" alt="Save image" />
</p>

Como podemos observar, la imagen se guardo en la ruta previamente seleccionada.

<p align="center">
  <img src="https://github.com/user-attachments/assets/18665985-404a-4675-91ad-68137afa6d13" alt="Image Saved" />
</p>


