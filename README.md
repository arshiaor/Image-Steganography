# Steganography
## Steganography is the art of hiding secret data in a file.
### In this project we are going to learn image steganography
![alt text](https://img.shields.io/badge/-Python-green)
![alt text](https://img.shields.io/badge/-Steganography-blue)
![alt text](https://img.shields.io/badge/-Security-yellow)
![alt text](https://img.shields.io/badge/-Image%20Proccessing-orange)
---
# How to use 
### To use this application you will  need python and pip package installed.
> ### Note! This code works for PNG formats beacues of compreesion in JPEG formats we might have dataloss.

### To start using this package first clone the repository.
> ### git clone https://github.com/arshiaor/Image-Steganography.git

### Then you have to install package dependancies by 
> ### pip install -r requirements.txt

### If you have virtual environment this will be fine to just run the program but if you want to run it as a script: 
> ### chmod +x steganography.py
> ### ./steganography.py 
---
# How the algorithm works

### An image consists of pixels. and each pixel has 3 bytes of values (red , gree, and blue ) in numbers of 0-255.

## Encoding
1. ### first we get the data that we want to hide and each character of data's ASCII code will be extracted and converted to 8-bit binaries.
2. ### Each time three pixels will be read. ( 3 x 3 = 9 RGB values) and we use the first 8 RGB values to store characters and the last value will tell us whether the message is completed or we would need to read another 3 pixels.(we will expand it later)
3. ### each RGB value will be compared with th fellow binary to see if the binary figit is 1, the value will be converted to odd or if the binary value is 0 the RGB value will be converted to even.

## For Example
### let's say our message is 'Hii'. <br >
### This message has 3 bytes so we will need 3 pixels to encode this( 3 x 3= 9 RGB values). for example consider we have 4x3 image with 12 pixels:
```
[(27, 64, 164), (248, 244, 194), (174, 246, 250), (149, 95, 232),
(188, 156, 169), (71, 167, 127), (132, 173, 97), (113, 69, 206),
(255, 29, 213), (53, 153, 220), (246, 225, 229), (142, 82, 175)]
```
## Steps:
### 1. the ASCII value of H is 72 so the binary will be 01001000
### 2. we read the first three pixels:
```
(27, 64, 164), (248, 244, 194), (174, 246, 250)
```
### 3. now we make changes to the RGB values. for example the first binary digit is 0 so the first RGB value should be changed from 27 o 26 to be even. jus tlike that 64 turns to 63 to be odd because th second binary number is 1 and so it continues.
> Note! we should be carefull about the RGB values to not fo far from 255 or bellow 0. 

### 4. now we should take care of the 9th RGb value, so if our message is ling and we need to continue reading 3 more pixels, the RGB value should be an even number but if the message is completed the 9th value should e odd.

## Decoding
### 1. Again three pixels will be read.and the ninth one gives us info to contiue reading or not.
### 2. for the values, if they are odd the binary bit is 1, and if they are even the binary bit is 0.
### 3. the bits will be concatenated to Strings 
### 4. if the ninth value is even we keep reading three more pixels or if not we stop.
## Sources: 
- https://betterprogramming.pub/image-steganography-using-python-2250896e48b9 <br>
- https://www.geeksforgeeks.org/program-decimal-binary-conversion/ <br>
- https://www.geeksforgeeks.org/working-images-python/ <br>