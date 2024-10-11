# Image Analyzer

This project is an image analysis tool that allows the application and removal of image noise using image processing algorithms.

## Previous requirements
Make sure you have installed

- OpenCV
- Numpy
- Tkinter
- PyQT5

To use the program, just execute the following command in cmd.

```cmd
python .\app.py
```

## Use of the program
When executing the previously shown command, the program menu should be displayed.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8cb5d2ce-94bc-4d17-a48a-e712f8303f23" alt="menu" />
</p>

Inside we will have the options to apply certain statistical filters and noises, the size of the kernel and the selection of the variables that are required in some filters and noises. It also allows the selection of the image to be modified, as well as the saving of the modified image.

## Program functions

### Application of the kernel

To apply the kernel, the value must be written in the corresponding box. It should be clarified that the value to be assigned must be thought about, since the larger the kernel, the longer it will take to obtain a result in the application of the filters.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a469c96b-de5f-42b6-956b-8b4cc880ff67" alt="Select Kernel" />
</p>

For the following examples, a 5x5 kernel will be used.

### Select image

For the example, we must first select an image. Click on the “Seleccionar imagen” button. A window for image selection will be displayed.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9824a9a6-e2f3-4bb3-b32b-cb9d7a8c3eed" alt="Image selection window" />
</p>

Select the image.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bb8f8c0e-d95e-4d53-9d37-76adc7ebdf1f" alt="Select image" />
</p>

The selected image will be displayed in the menu.

<p align="center">
  <img src="https://github.com/user-attachments/assets/904dd4a0-24df-4287-80b6-4484effaeb82" alt="Selected image in menu" />
</p>

Once the image is selected and the kernel is applied, you can proceed to apply the filters.

### Maximum filter

Click on the “Filtro max” button to apply the statistical filter on the image.

<p align="center">
  <img src="https://github.com/user-attachments/assets/92816f3f-c8d4-4589-8443-f81b2626490a" alt="Max filter applied" />
</p>



### Minimum filter

Click on the “Filtro min” button to apply the statistical filter on the image.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2455ed08-c331-4108-be3f-0a94e1fee723" alt="Min filter applied" />
</p>



### Midpoint filter

Click on the “Filtro punto medio” button to apply the statistical filter on the image.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec4acc4e-ed85-4f96-812a-32aff4aacd77" alt="Median filter" />
</p>


### Alpha-Trimmed Mean Filter

In this filter we must declare a value for d, as long as the value is not greater than the kernel dimension (mxn), we declare a value of 10.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b6474b62-c430-4e0f-82a0-8a9df9cdd97c" alt="Select d" />
</p>

Now we can apply the filter by clicking on the "Filtro Medio de Corte Alfa" button.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b5da02b-eca3-46a0-9806-cff616bbbfa4" alt="Alpha-Trimmed Mean Filter" />
</p>


### Uniform Noise

To apply the Uniform Noise we must declare the variables a and b. The variables must be in a range from 0 to 255, and b must be greater than the variable a.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a7b6eb66-0ca3-4f2f-ba3a-afac786479b8" alt="Select Uniform Noise" />
</p>

With the variables declared, we apply the noise by clicking on the “Ruido uniforme” button.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a06bf225-070b-4819-b6f5-420ea30dd30e" alt="Uniform Noise" />
</p>


### Exponential Noise

To apply the Exponential Noise we must declare the variables a. The variable must be in a range from 0 to 255.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b80daf91-b54b-457d-9fe5-1f1e5051d23f" alt="Select Exponential Noise" />
</p>

Now we can apply the noise by clicking on the “Ruido Exponencial” button.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9fa2dcdf-e1f0-4607-8a35-86f0a61e54e4" alt="Exponential Noise" />
</p>


### Save image

If you want to save the result, click on the “Save image” button. A window for saving the image will be displayed, where you can change the image name and extension if necessary.

<p align="center">
  <img src="https://github.com/user-attachments/assets/315f0e77-50ba-4b85-b879-36c6e663f2b2" alt="Save image" />
</p>

As we can see, the image is saved in the previously selected path.

<p align="center">
  <img src="https://github.com/user-attachments/assets/18665985-404a-4675-91ad-68137afa6d13" alt="Image Saved" />
</p>

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
