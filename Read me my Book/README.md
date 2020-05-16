# Read Me My Book App

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## Introduction

These days there is a huge demand in storing the information available in paper documents into a computer, storage disk and then later reusing this information by searching process. One simple way to store information from these paper documents in to computer system is to first scan the documents and then store them as images. But to reuse this information it is very difficult to read the individual contents and searching the contents form these documents line-by-line and word-by-word.This poses an inconvenience because the image is not searchable or editable. Even when we want to convert scanned images directly into pdf, they are not in editable or searchable format.

The aim of this project was to make a software which would be capable of identifying and recognizing English typed text from an image(.jpg, .jpeg, .png) and convert it to an editable format(.txt ,etc) so that it can be directly modified without the need for typing the text document again manually. The project involves the implementation of Image Processing techniques and Machine Learning Algorithms.

## Approach:

 * Image Processing:
   <ol>
    <li>Binarization</li>
    <li>Skew-Correction</li>
   </ol>
 * Segmentation 
   <ol>
    <li>Line segmentation</li>
    <li>Character segmentation</li>
   </ol>
 * The training is done using CNN model.

## To install
The language used is Python3
  
  ### Required libraries
  ```sh
      Numpy
      OpenCV
      Sklearn
      Scikit
      Tensorflow
      PyQt4
```
  ### To run through GUI
  ```sh
      python gui.py      
```
  ### To run on CLI
  ```sh
      python main.py     
```

### Authors

[Aniket Kumar](https://github.com/roshniRam)

[<img src="https://image.flaticon.com/icons/svg/185/185961.svg" width="35" padding="10">](https://twitter.com/AniketK32848136)
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/aniketkumar3655/)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/aniket_pathakk/)
